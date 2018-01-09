<template>
  <div>
    <Topbar :showArrow="showArrow" :goBack="$store.state.backPath.thirdPath" :headText="book && book.title" :showFun="showFun"></Topbar>

    <pulse-loader :loading="loading" :color="color" :size="size" :margin="margin"></pulse-loader>

    <transition name="fade">
      <section v-show="!loading">

        <!-- book name and so on -->
        <img v-if="book" :src="staticPath + book.cover">

        <div class="book-info">
          <p class="book-title" v-if="book">{{book.title}}</p>
          <p class="book-author" v-if="book">{{book.author}}</p>
          <p class="reader-info" v-if="book">
            <!-- {{book.updated}} | ago -->
            <span v-text=""></span>{{book.updated}} | {{wordCount}}万字 | {{book.cat}}</p>
        </div>

        <!-- button -->
        <div class="book-operation">
          <button class="btn" @click="readBook">开始阅读</button>
          <button class="btn" @click="followAction">{{isFollowed ? '从书架移除' : '加入书架'}}</button>
          <button class="btn" @click="showChapter">{{isShowChapter ? '隐藏目录' : '显示目录'}}</button>
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

        <!-- tag -->
        <div class="book-tag" v-if="book">
          <span v-for="(tag, index) in book.tags" :key="index" class="tag">{{tag}}</span>
        </div>
        
        <!-- detail -->
        <article class="book-intro" v-if="book" v-html="bookChaptersBody" margin-left="5vw"></article>
      
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
                    <div class="title">{{chapter.title}}</div>
                    <div class="title2">&nbsp;{{chapter.title2}}</div>
                </v-touch>
                <div v-else class="mulucenter">
                    {{chapter.title}}
                </div>
                </v-touch>
            </ul>
      </div>
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
      this.$router.push('/readbook/' + this.$route.params.bookId);
    },
    jumpChapter(index) {
      this.$store.commit('setReadBook',this.book);
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
        delete localShelf[this.book._id];
        //重新保存
        storage.setItem("followBookList", JSON.stringify(localShelf));
        this.isFollowed = !this.isFollowed;
      } else {
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
  width: 5rem;
  height: 6rem;
  float: left;
  margin-right: 0.4rem;
}

section {
  box-sizing: border-box;
  padding-right: 1rem;
  padding-left: 1rem;
  padding-bottom: 0.2rem;
  padding-top: 0.2rem;
  margin-top: 3.5rem;
  width: 100vw;
}

section:first-child {
  margin-bottom: 1rem;
}

.book-info {
  box-sizing: border-box;
  width: 100%;
  height: 6rem;
  padding-left: 6rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.book-info p {
  margin: 0;
  line-height: 1.8rem;
}

.book-operation {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding-top: 3rem;
  padding-bottom: 3rem;
  border-bottom: 1px solid #f2f2f2;
}

.book-operation .btn {
  width: 6rem;
  background: #03a9f4;
  border: none;
  color: #fff;
  font-size: 1rem;
  text-align: center;
  line-height: 2.2rem;
  border-radius: .2rem;
}

.book-operation .btn:focus {
  background: #2196f3;
  outline: none;
}

.book-status {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  padding: 1rem 0;
  border-bottom: 1px solid #f2f2f2;
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
  margin-top: 1rem;
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
    font-size: 0.5rem;
    color: #807d7d;
}
.mulucenter {
    text-align: center;
}

</style>
