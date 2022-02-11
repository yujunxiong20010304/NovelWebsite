<template>
  <div id="home">
    <Affix :offset-top="0">
      <div id="header">
        <div id="navigation_one">
          <Menu mode="horizontal" theme="light" :active-name="Indexs" style="height:61px;" @on-select="openMenu">
              <MenuItem name="/home/bookcity" to="/home/bookcity">
                  <Icon type="md-bookmarks" />
                  首页
              </MenuItem>
              <MenuItem name="/home/fflt" to="/home/fflt">
                  <Icon type="ios-bonfire" />
                  限时免费
              </MenuItem>
              <MenuItem name="/home/novelclassification" to="/home/novelclassification">
                  <Icon type="logo-buffer" />
                  小说分类
              </MenuItem>
              <MenuItem name="/home/mybookcity" to="/home/mybookcity">
                  <Icon type="ios-leaf" />
                  个人主页
              </MenuItem>
          </Menu>
        </div>
        <div id="navigation_two">
          <div id="search">
            <a-input placeholder="搜索书籍"
                     v-model="seach"
                     style="width:275px;
                     border-top-right-radius: 0;
                     border-bottom-right-radius: 0;"/>
            <Button type="primary"
                    :to="{path:'/home/query',query:{search:this.seach}}"
                    style="border-top-left-radius: 0;
                     border-bottom-left-radius: 0;">
              搜索
            </Button>
          </div>
          <div id="state">
            <nologin v-if="false"></nologin>
            <surelogin v-if="user"></surelogin>
            <nologin v-else></nologin>
          </div>
        </div>
      </div>
    </Affix>
    <router-view></router-view>
  </div>
</template>
<script>
import nologin from '@/views/head/judge/nologin'
import surelogin from '@/views/head/judge/surelogin'
export default {
  components: { nologin, surelogin },
  data () {
    return {
      Indexs: '/home/bookcity',
      seach: '',
      user: ''
    }
  },
  methods: {
    /* 首页导航的方法 */
    openMenu (e) {
      this.Indexs = e
    },
    /* 获取session */
    async trial () {
      const { data: res } = await this.$http.post('/trial')
      this.user = res.username
      this.$store.commit('name', res.username)
    }
  },
  created () {
    this.trial()
    let pathParagraph = this.$route.path.split('/')
    this.Indexs = '/' + pathParagraph[1] + '/' + pathParagraph[2]
  },
  watch: {
    $route: {
      handler (val, oldVal) {
        this.Indexs = '/' + val.path.split('/')[1] + '/' + val.path.split('/')[2]
      },
      immediate: true
    }
  }
}
</script>
<style scoped lang="less">
#header{
  width: 1280px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #DCDEE2;
  box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.5);
  margin-bottom: 3px;
  background-color: #fff;
}
#navigation_one {
  width: 452px;
  height: 60px;
  min-width: 452px;
  margin-left: 15px;
}
#navigation_two {
  width: 55%;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  #state {
    width: 225px;
    height: 60px;
    line-height: 60px;
    min-width: 225px;
    display: flex;
    align-items: center;
  }
  #search {
    width: 335px;
    min-width: 335px;
    align-items: center;
    display: flex;
  }
}
</style>
