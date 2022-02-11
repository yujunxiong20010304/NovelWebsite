<template>
  <!-- 我的书架 -->
  <header>
    <div id="personalbookshelf">
      <div id="head">
        <div style="width: 60px;margin-left: 5px;">选择</div>
        <div style="width: 125px;">书名</div>
        <div style="width: 36px;">类型</div>
        <div style="width: 105px;">作者</div>
        <div style="width: 185px;">最新章节</div>
        <div style="width: 185px;">当前章节</div>
        <div style="width: 54px;">状态</div>
        <div style="width: 145px;">操作</div>
      </div>
      <div id="content" v-for="(i,index) in collectBooks" :key="i.book_id">
        <a-checkbox style="width: 60px;margin-left: 5px;" v-model="check[index]"></a-checkbox>
        <div style="width: 125px;">{{i.book_name}}</div>
        <div style="width: 36px;">{{i.book_type}}</div>
        <div style="width: 105px;">{{i.book_author}}</div>
        <div style="width: 185px;">{{i.book_new_chapter}}</div>
        <div style="width: 185px;">{{i.book_old_chapter}}</div>
        <div style="width: 54px;">连载中</div>
        <div style="width: 145px; display: flex;justify-content: flex-start;">
          <Button type="error" ghost size="small" @click="singleDeletion([i.book_id])">删除</Button>
          <Button type="info" ghost size="small" style="margin-left: 15px;" :to="{path:'/home/read',query:{num:i.num,type:i.book_type,name:i.book_name,author:i.book_author,time:i.updatetime}}">阅读</Button>
        </div>
      </div>
    </div>
    <div id="bottomNavigation">
      <div id="delete">
        <a-checkbox style="width: 60px;margin-left: 5px;" @change="fullControl" v-model="all">全选</a-checkbox>
        <div @click="allDelete">删除</div>
      </div>
      <a-pagination simple :default-current="1" :total="allCurrent" style="margin-right: 15px;" v-model="current"/>
    </div>
  </header>
</template>

<script>
export default {
  name: 'personalbookshelf',
  data () {
    return {
      user: '',
      collectBooks: '',
      check: { 0: false, 1: false, 2: false, 3: false, 4: false, 5: false, 6: false, 7: false },
      num: 8, // 当前渲染的数据条数，视后端能传来的为主
      all: false, // 全选
      current: 1, // 当前页码
      allCurrent: 20 // 总页码
    }
  },
  watch: {
    check: {
      handler () {
        let judge = null
        let body = []
        for (let i = 0; i < this.num; i++) {
          body[i] = this.check[i]
          judge = body.every(val => val)
        }
        this.all = judge
      },
      immediate: true,
      deep: true
    },
    current: {
      handler () {
        this.collection()
        for (let i = 0; i < this.num; i++) {
          this.check[i] = false
        }
      },
      immediate: true
    }
  },
  methods: {
    fullControl (e) {
      for (let i = 0; i < this.num; i++) {
        this.check[i] = e.target.checked
      }
    },
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
    }, /* 获取收藏图书数据,需要的参数：1.用户名 2.当前的页数 */
    async collection () {
      const { data: res } = await this.$http.get('/getBookshelf', { params: { user: this.user, page: this.current } })
      if (res.code === 200) {
        this.allCurrent = (res.body[1]['count(*)'] / 8) > parseInt((res.body[1]['count(*)'] / 8)) ? (parseInt((res.body[1]['count(*)'] / 8)) + 1) * 10 : parseInt((res.body[1]['count(*)'] / 8)) * 10
        this.collectBooks = res.body[0]
        this.num = res.body[0].length
      }
    },
    /* 单删按钮 参数：是要删除的小说的id，但是放进了列表里 */
    singleDeletion (datas) {
      this.delete(datas)
      this.trial()
      setTimeout(() => {
        this.collection()
      }, 500)
      for (let i = 0; i < this.num; i++) {
        this.check[i] = false
      }
    },
    /* 删除 */
    async delete (datas) {
      let { data: res } = await this.$http.get('/delete', { params: { id: datas[0] } })
      if (res.code === 400) {
        console.log(res.message)
      }
    },
    allDelete () {
      let toBeDeleted = []
      for (let i = 0; i < this.num; i++) {
        if (this.check[i] === true) {
          toBeDeleted[toBeDeleted.length] = i
        }
      }
      let datas = []
      for (let i = 0; i < toBeDeleted.length; i++) {
        datas[datas.length] = this.collectBooks[toBeDeleted[i]].book_id
      }
      this.delete(datas)
      this.trial()
      setTimeout(() => {
        this.collection()
      }, 500)
      for (let i = 0; i < this.num; i++) {
        this.check[i] = false
      }
    }
  },
  created () {
    this.trial()
    setTimeout(() => {
      this.collection()
    }, 1000)
  }
}
</script>

<style scoped lang="less">
header {
  width: 100%;
  height: 500px;
  background-color: #d6d6d6;
  margin: 25px 25px 0 25px;
  #bottomNavigation {
    width: 100%;
    display: flex;
    align-items: center;
    height: 50px;
    justify-content: space-between;
    background-color: #F7F7F7;
    #delete {
      display: flex;
      width: 150px;
      height: 100%;
      justify-content: space-between;
      align-items: center;
      div {
        border: 1px solid #d6d6d6;
        width: 72px;
        height: 26px;
        text-align: center;
        line-height: 26px;
        font-size: 12px;
        color: #999;
        &:hover {
          color: #333333;
        }
      }
    }
  }
}
#personalbookshelf {
  width: 100%;
  border-radius: 5px;
  height: 451px;
  #head,#content {
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-between;
    text-align: left;
    height: 50px;
    background-color: #eee;
  }
  #head {
    font-size: 16px;
    background-color: lightseagreen;
    color: #fff;
  }
  #content {
    font-size: 14px;
    color: #515a6e;
    border-bottom: 1px solid #E0DEDA;
    div {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    &:hover {
      background-color: #C6C8D1;
      color: white;
    }
  }
  #turnPages {
    display: flex;
    justify-content: space-between;
  }
}
</style>
