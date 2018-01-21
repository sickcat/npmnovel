<template>
  <div>
    <Topbar :showArrow="showArrow" :goBack="$store.state.backPath.thirdPath" :headText="book && book.title" :showFun="showFun"></Topbar>

    <pulse-loader :loading="loading" :color="color" :size="size" :margin="margin"></pulse-loader>

    <transition name="fade"> 
      <section v-show="!loading">

        <!-- book name and so on -->
        <div class="back-blue">
          <img v-if="book" :src="staticPath + book.cover">

          <div class="book-info">
            <p class="book-title" v-if="book">{{book.title}}</p>
            <p class="book-line"></p>
            <p class="book-author" v-if="book">{{book.author}}</p>
            <p class="reader-info" v-if="book">
              <!-- {{book.updated}} | ago -->
              <span v-text=""></span>{{book.updated}} | {{wordCount}}万字 | {{book.cat}}</p>
          </div>
        </div>
        <!-- statics -->
        <div class="book-status">
          <div class="list-item">
            <span class="item">阅读人次</span>
            <span v-if="book">{{book.read_count}}</span>
          </div>
          <div class="list-item">
            <span class="item">点击人次</span>
            <span v-if="book">{{book.click_count}}</span>
          </div>
          <div class="list-item">
            <span class="item">最后更新章节</span>
            <span v-if="book">{{book.lastChapter}}</span>
          </div>
        </div>

        <!-- button -->
        <div class="book-operation">
          <button class="btn" @click="readBook">
            <img class="btn-img" src="/static/png/startreading.png">
          </button>
          <!--button class="btn" @click="followAction">{{isFollowed ? '从书架移除' : '加入书架'}}</button-->
          <button class="btn" @click="followAction" :class="{ backblue: isFollowed}">
            <img class="btn-img" src="/static/png/addtocraft.png">
          </button>
          <button class="btn" @click="showChapter">
            <img class="btn-img" src="/static/png/showcat.png">
          </button>
          <!--button class="btn" @click="showChapter">{{isShowChapter ? '隐藏目录' : '显示目录'}}</button-->
        </div>


        <!-- tag -->
        <!--div class="book-tag" v-if="book">
          <span v-for="(tag, index) in book.tags" :key="index" class="tag">{{tag}}</span>
        </div-->
        <div class="book-des">
          <div class="vertical-line">
            &nbsp;&nbsp;<b>书籍简介&nbsp;：</b>
          </div>
        </div>
        <!-- detail -->
        <div v-show="!isShowChapter">
          <article class="book-intro" v-if="book" v-html="bookChaptersBody" style="font-family: '宋体'"></article>      
        </div>
      
      </section>
      <!--<section></section>-->
    </transition>

    <div class="chapter-list" v-show="isShowChapter" v-scroll="onScroll">
            <div class="chapter-contents">
                <p>{{$store.state.bookInfo.title}}：目录</p>
                <v-touch tag="span" class="chapter-sort" @tap="descSort">
                    <Icon type="arrow-down-b" v-if="!chapterDescSort"></Icon>
                    <Icon type="arrow-up-b" v-else></Icon>
                </v-touch>
            </div>
            <ul id="chapter-list">
                <v-touch tag="li" v-if="loadedChapters" v-for="(chapter, index) in loadedChapters" :key="index">
                <v-touch v-if="chapter.click" @tap="jumpChapter(index)">
                    <div class="title">&nbsp;·&nbsp;{{chapter.title}}</div>
                    <div class="title2">&nbsp;&nbsp;&nbsp;{{chapter.title2}}</div>
                </v-touch>
                <div v-else class="mulucenter">
                    {{chapter.title}}
                </div>
                </v-touch>
            </ul>
      </div>
      <v-touch class="hide-chapter" v-show="isShowChapter" @tap="hideShow">
      </v-touch>
  </div>
</template>

<script>
import Topbar from './Topbar'
import api from '../libs/api'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import moment from 'moment'

export default {
  name: 'Book',
  components: {
    Topbar,
    PulseLoader
  },
  data() {
    return {
      showArrow: true,
      showFun: false,
      book: null,
      staticPath: api.staticPath,
      isFollowed: false,
      loading: true,
      color: '#04b1ff',
      size: '10px',
      margin: '4px',
      isShowChapter: false,
      loadedChapters: [],
      bookChapter: {},
      chapterDescSort: false, //是否降序排列
      loadPages: 0,
    }
  },
  filters: {
    ago(time) {
      return moment(time).fromNow();
    }
  },
  computed: {
    wordCount() {
      return parseInt(this.book.wordCount / 10000, 10);
    },
    bookChaptersBody() {
      return this.book.longIntro.replace(/\n/g, '<br>').replace(/ /g,'&nbsp;');
    }
  },
  created() {
    api.getBook(this.$route.params.bookId).then(response => {
      this.book = response.data;
      console.log(this.book)
      this.loading = false;
      this.isFollowBook();
    }, err => {
      console.log(err)
    });
    api.getMixChapters(this.$route.params.bookId).then(response => {
            //console.log(response.data)
            this.bookChapter = response.data;
            //缓存时默认取前50章节
            this.loadedChapters = this.bookChapter.chapters;
            //console.log(this.loadedChapters)
            this.currentChapter = readRecord && readRecord[this.$route.params.bookId] && readRecord[this.$route.params.bookId].chapter ? readRecord[this.$route.params.bookId].chapter : 0;
            this.getBookChapterContent();
        }).catch(err => {
            console.log(err);
        });
  },
  beforeRouteEnter(to, from, next) {  
    next(vm => {
      if(from.fullPath.indexOf('/readbook/') === -1){
          vm.$store.commit('setThirdPath',from.fullPath);     
      }
    })
  },
  methods: {
    onScroll: function (e, position) {
      
    },
    readBook() {
      this.$store.commit('setReadBook',this.book);
      this.$store.commit('setTitle',this.book.title);
      this.$router.push('/readbook/' + this.$route.params.bookId);
    },
    jumpChapter(index) {
      this.$store.commit('setReadBook',this.book);
      this.$store.commit('setTitle',this.book.title);
      this.$router.push('/readbook/' + this.$route.params.bookId + '/' + index);
    },
    showChapter() {
      this.isShowChapter = !this.isShowChapter;
    },
    hideShow() {
      this.isShowChapter = false;
    },
    //章节倒叙查看
    descSort() {
        this.chapterDescSort = !this.chapterDescSort;
        this.bookChapter.chapters.reverse();
        this.loadedChapters = this.bookChapter.chapters;
        this.loadPages = 1;
    },
    isFollowBook() {
      //返回本地是否缓存（加入书架）
      let localShelf = JSON.parse(window.localStorage.getItem('followBookList'));
      this.isFollowed = localShelf && localShelf[this.book._id] ? true : false;
    },
    followAction() {
      let storage = window.localStorage;
      let localShelf = JSON.parse(storage.getItem('followBookList')) ? JSON.parse(storage.getItem('followBookList')) : {};
      if (this.isFollowed) {
        //删除该书籍在本地的缓存记录
        this.$Message.info('已从书架删除');
        delete localShelf[this.book._id];
        //重新保存
        storage.setItem("followBookList", JSON.stringify(localShelf));
        this.isFollowed = !this.isFollowed;
      } else {
        this.$Message.info('加入书架成功');
        // 以bookId为键值，方便后续删除等操作
        localShelf[this.book._id] = {
          cover: this.book.cover,
          title: this.book.title
        }
        storage.setItem("followBookList", JSON.stringify(localShelf));
        this.isFollowed = !this.isFollowed;
      }
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
  width: 6rem;
  height: 9rem;
  float: left;
  margin-right: 0.4rem;
}

section {
  box-sizing: border-box;
  padding-bottom: 0.2rem;
  padding-top: 0.2rem;
  margin-top: 2.9rem;
  width: 100vw;
}

section:first-child {
  margin-bottom: 1rem;
}

.back-blue {
  padding-top: 1rem;
  padding-left: 1rem;
  width: 100vw;
  height: 11em;
  background: #005390;
}

.backblue {
  background: #005390;
  color: #005390;
}

.book-info {
  box-sizing: border-box;
  width: 100%;
  height: 9rem;
  padding-left: 7.5rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  color: #ffffff;
}

.book-info p {
  margin: 0;
  line-height: 1.8rem;
}

.book-title {
  font-size: 1.3rem;
}

.book-author {
  font-size: 0.8rem !important;
}

.book-line {
  margin-top: 1rem;
  width: 5rem;
  border: 1px solid #f2f2f2;
}

.book-operation {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding-top: 3rem;
  padding-bottom: 3rem;
  border-bottom: 1px solid #f2f2f2;
  margin-bottom: 3rem;
  z-index: 100;
}

.book-operation {
  width: 100vw;
  border: none;
  color: #fff;
  font-size: 1rem;
  text-align: center;
  line-height: 1rem;
  border-radius: .2rem;
}

.btn {
  width: 6rem;
  background: #ffffff;
  border: none;
  color: #fff;
  font-size: 1rem;
  text-align: center;
  height: 1rem;
  border-radius: .2rem;
  outline: none;
}

.btn-img {
  width: 6rem;
  height: 2rem;
  float: left;
  margin-right: 0.4rem;
}

.book-operation:focus {
  background: #2196f3;
  outline: none;
}

.book-status {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  padding: 1rem 0;
  width: 95vw;
  margin-left: 2.5vw;
  margin-right: 2.5vw;
  border-bottom: 1px solid #B1B1B1;
}

.vertical-line {
  margin-left: 2vw;
  border-left: 0.5rem solid #005390;
}

.list-item {
  display: flex;
  flex-direction: column;
  width: 33%;
  text-align: center;
}

.item {
  font-size: .8rem;
  color: #807070;
}

.book-tag {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  flex-wrap: wrap;
  padding: .6rem 0 0;
  border-bottom: 1px solid #f2f2f2;
}

.tag {
  padding: .2rem .7rem;
  color: #fff;
  border-radius: .1rem;
  margin-bottom: .6rem;
  font-size: 0.8rem;
  margin-left: .4rem;
}

.tag:nth-child(1n) {
  background: burlywood;
}

.tag:nth-child(2n) {
  background: cadetblue;
}

.tag:nth-child(3n) {
  background: coral;
}

.tag:nth-child(4n) {
  background: cornflowerblue;
}

.reader-info,.book-author {
  font-size: 0.9rem;
}
.book-intro{
  margin-top: 0.5rem;
  padding-left: 5vw;
  padding-right: 5vw;
  font-size: 1.1rem;
}
.chapter-list {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    overflow: auto;
    background: #fff;
    width: 80vw;
}

.chapter-list ul {
    margin-top: 2.5rem;
}

.chapter-list li {
    padding-top: 2.5rem;
    padding-left: 1rem;
    line-height: 2.5rem;
    border-bottom: 1px solid #f2f2f2;
}

.chapter-contents {
    position: fixed;
    top: 0;
    left: 0;
    width: 80vw;
    background: #fff;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    line-height: 2.5rem;
    padding-left: 1rem;
}
.chapter-contents-2 {
    position: fixed;
    top: 0;
    left: 0;
    width: 80vw;
    background: #fff;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    line-height: 2.5rem;
    padding-left: 1rem;
}

.chapter-sort {
    margin-right: 1.5rem;
    font-size: 1.4rem !important;
}

.title {
    font-size: 1rem;
    color: #000000;
}

.title2 {
    font-size: 0.8rem;
    color: #807d7d;
}
.mulucenter {
    text-align: center;
}
.hide-chapter {
  position: fixed;
  right: 0;
  top: 0;
  height: 100vh;
  width: 20vw;
}
</style>
