<template>
  <div id="rank">
    <slot name="default"></slot>

    <ol class="drawer" @mouseleave="close" @mouseenter="open">
      <li @mouseenter="openMenu" @mouseleave="closeMenu" id="one" v-if="book">
        <div class="hed">
          <div class="num">1</div>
          <span class="h">{{book[0].title}}</span>
        </div>
        <span class="category">{{book[0].category}}</span>
        <div class="book">
          <div class="content">
            <span style="margin-top:5px;">{{book[0].author}}</span>
            <span style="margin-top:15px;">{{book[0].category}}</span>
          </div>
          <router-link :to="{path:'/home/designatedBook',query:{type:book[0].category,name:book[0].title}}">
            <img :src="book[0].chart" alt=""/>
          </router-link>
        </div>
      </li>
      <li @mouseenter="openMenu" @mouseleave="closeMenu" id="two" v-if="book">
        <div class="hed">
          <div class="num">2</div>
          <span class="h">{{book[1].title}}</span>
        </div>
        <span class="category">{{book[1].category}}</span>
        <div class="book">
          <div class="content">
            <span style="margin-top:5px;">{{book[1].author}}</span>
            <span style="margin-top:15px;">{{book[1].category}}</span>
          </div>
          <router-link :to="{path:'/home/designatedBook',query:{type:book[1].category,name:book[1].title}}">
            <img :src="book[1].chart" alt=""/>
          </router-link>
        </div>
      </li>
      <li v-for="(i,index) in book.slice(2,10)" :key="index" @mouseenter="openMenu" @mouseleave="closeMenu" :class="index===1?'judge':''">
        <div class="hed">
          <div class="num">{{index+3}}</div>
          <span class="h">
            <router-link style="color:initial;" :to="{path:'/home/designatedBook',query:{type:i.category,name:i.title}}">
              {{ i.title }}
            </router-link>
          </span>
        </div>
        <span class="category">{{ i.category }}</span>
        <div class="book">
          <div class="content">
            <span style="margin-top:5px;">{{ i.author }}</span>
            <span style="margin-top:15px;">{{ i.category }}</span>
          </div>
          <router-link :to="{path:'/home/designatedBook',query:{type:i.category,name:i.title}}">
            <img :src="i.chart" alt=""/>
          </router-link>
        </div>
      </li>
    </ol>
    <div id="more">查看更多</div>
  </div>
</template>

<script>
export default {
  name: 'rank',
  props: ['book'],
  data () {
    return {
    }
  },
  methods: {
    openMenu (e) {
      let div = e.target.querySelector('.book')
      let category = e.target.querySelector('.category')
      e.target.style.height = '135px'
      e.target.style.display = 'block'
      div.style.display = 'flex'
      category.style.display = 'none'
    },
    closeMenu (e) {
      let category = e.target.querySelector('.category')
      category.style.display = 'inline'
      let div = e.target.querySelector('.book')
      e.target.style.height = '38px'
      e.target.style.display = 'flex'
      div.style.display = 'none'
    },
    close (e) {
      let li = e.target.querySelector('#one')
      li.style.display = 'block'
      li.style.height = '135px'
      let book = li.querySelector('.book')
      book.style.display = 'block'
      let category = li.querySelector('.category')
      category.style.display = 'none'
    },
    open (e) {
      let li = e.target.querySelector('#one')
      li.style.display = 'flex'
      li.style.height = '38px'
      let book = li.querySelector('.book')
      book.style.display = 'none'
      let category = li.querySelector('.category')
      category.style.display = 'inline'
    }
  }
}
</script>

<style scoped lang="less">
#rank {
  width: 278px;
  height: 645px;
  margin-right: 20px;
  background-color: #FCFBF9;
  border-radius: 10px;
  #more {
    width: 100%;
    height: 43px;
    text-align: center;
    line-height: 43px;
    margin-top: 15px;
    color: #389EAC;
    &:hover {
      background-color: #eff2f3;
      cursor: pointer;
    }
  }
  .drawer {
    width: 238px;
    height: 476px;
    list-style-type:none;
    display: flex;
    flex-wrap: wrap;
    margin: 0 auto;
    .hed {
      display: flex;
      align-items: center;
    }
    #one {
      width: 100%;
      height: 135px;
      display: block;
      .num {
        color: #FA595F;
      }
      .book {
        display: flex;
      }
      .category {
        display: none;
      }
    }
    #two {
      .num {
        color: #FF9E2C;
      }
    }
    li {
      position: relative;
      width: 100%;
      height: 38px;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      .num {
        font-weight:bold;
        font-size: 14px;
        width:20px;
        display:inline-block;
        color: #F9C300;
      }
      .h {
        font-size: 14px;
        color: #333333;
        font-weight: normal;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: inline-block;
        width: 100px;
      }
      .category {
        position:absolute;
        right:0;
        font-size:12px;
        color:#777;
      }
      .book {
        display: none;
        /*display: none;*/
        .content {
          display: flex;
          flex-wrap: wrap;
          margin-left: 20px;
          font-size: 12px;
          color: #777;
          span {
            width: 100%;
          }
        }
        img {
          border-radius: 5px;
          width: 80px;
          height: 120px;
          position: absolute;
          top: 10px;
          right: 0;
          box-shadow:0 15px 35px rgba(0,0,0,0.1),0 3px 10px rgba(0,0,0,0.09);
        }
      }
    }
  }
}
</style>
