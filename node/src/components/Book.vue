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
            <!--p class="book-line"></p-->
            <p class="book-author" v-if="book">{{book.author}}</p>
            <p class="reader-info" v-if="book">
              <!-- {{book.updated}} | ago -->
              <span v-text=""></span>出版时间：{{book.updated}} &nbsp;| &nbsp;{{wordCount}}万字</p>
            <p class="ago" v-if="book">
              <div class="ago" v-if="!hasHistory">&nbsp;暂未阅读</div>
              <div class="ago" v-if="hasHistory">&nbsp;{{Tago}},阅读到{{chapterTitle}}</div>
            </p>
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
        <div class = "bottom-container">        
          <div class="book-des">
            <div class="vertical-line">
              &nbsp;&nbsp;<b>书籍简介&nbsp;：</b>
            </div>
          </div>
          <p>&nbsp;&nbsp;</p>
          <!-- detail -->
          <div v-show="!isShowChapter">
            <article class="book-intro" v-if="book && !showimg" v-html="bookChaptersBody"></article> 
            <img v-else src="/static/png/long-info.png" class="long-intro-img">
          </div>

          <div v-show="!isShowChapter">
            <div>
              <h3 class="comment-head">评论</h3>
              <p class="comment comment-name" v-if="comment.length==0">暂无评论</p>
              <div v-else>
                <div class="comment" v-for="(item,index) in comment" v-bind:index="index" >
                  <b class="comment-name">{{item.name}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{item.time}}</b>
                  <p @click="changCommmer(item.name,index,item.id)">{{item.content}}</p>
                  <div v-if="item.reply.length > 0">
                    <div class="reply" v-for="reply in item.reply">
                        <b class="comment-name">{{reply.responder}}&nbsp;&nbsp;回复&nbsp;&nbsp;{{reply.reviewers}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{reply.time}}</b>
                        <p @click="changCommmer(reply.responder,index, reply.id)">{{reply.content}}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="commentBox">
              <h3 class="comment-head">发表评论</h3>
              <div v-if="type" class="post-relpy">
              <b>你回复&nbsp;{{name}}</b>
              </div>
              <input type="text" placeholder="输入你的名字" v-model="commentName" class="post-name">
              <textarea name="" value="请填写评论内容" v-model="commentText" class="post-content"></textarea>
              <div class="post-button">
              <button @click="addComment" class="post-button-one">发表</button>
              <button @click="canelComment" class="post-button-one">取消</button>
              </div>
            </div>


          </div>
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
    PulseLoader,
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
      showimg: 0,
      hasHistory: false,
      Tago: "3天前",
      chapterTitle: "后记",
      comment: [
    	{
        	name: "有毒的黄同学",    //评论人名字
        	time: "2016-08-17",    
        	content: "好,讲得非常好，good",
        	reply: [              //回复评论的信息，是一个数组，如果没内容就是一个空数组
            {
                responder: "傲娇的",    //评论者
                reviewers: "有毒的黄同学",         //被评论者
                time: "2016-09-05",
                content: "你说得对"
            }
        	]
      	}
    ],
      type: 0,
      name: "测试名字1",
      commentText: "",
      commentName: "",
      replyid: 0,
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
      if (this.book.longIntro.indexOf("徐文海") != -1)
        this.showimg = 1;

      let readRecord = JSON.parse(window.localStorage.getItem('followBookList'));
      if (readRecord[this.$route.params.bookId].readTime) {
        this.hasHistory = true;
        this.Tago = moment(readRecord[this.$route.params.bookId].readTime).fromNow();
        this.chapterTitle = readRecord[this.$route.params.bookId].chapterTitle;
      }
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
    if(this.$route.query.user_id) {
      console.log(this.$route.query.user_id);
      this.$store.commit('setUserId',this.$route.query.user_id);
    } else {
      console.log("default");
    };
    api.getComment(this.$route.params.bookId).then(response => {
    	this.comment = response.data.comment;
    }).catch(err => {
    	console.log(err);
    });
  },
  beforeRouteEnter(to, from, next) {
    console.log(to);
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
    },
    addComment: function() {
      this.$emit("submit",this.commentText);
      this.commentText = "";
    },
    canelComment: function() {
      this.$emit("canelCommit");
      this.commentText = "";
      this.commentName = "";
      this.type = 0;
    },
    //添加评论
    addComment: function(data) {
      if (this.commentText == "" || this.commentName == "") {
        this.$Message.info('请输入名字及需要发表的内容');
        return;
      }
      data = new Object();
      data.name = this.commentName;
      data.content = this.commentText;
      data.replyid = this.replyid;
      data.rtype = this.type;
      api.postComment(this.$route.params.bookId, JSON.stringify(data)).then(response => {
        location.reload();
      });
    },
    //监听到了点击了别人的评论
    changCommmer: function(name,index, id) {
        this.name = name;
        this.type = 1;
        this.replyid = id;
    },
    //监听到了取消评论
    canelCommit: function() {
      this.type = 0;
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
  padding-left: 6.5rem;
  padding-bottom: 0.5rem;
  color: #ffffff;
}

.book-info p {
  margin: 0;
}

.book-title {
  font-size: 1.1rem;
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
  border-bottom: 1px solid #f2f2f2;
  z-index: 1000;
  height: 9rem;
  width: 100vw;
  border: none;
  color: #fff;
  border-radius: .2rem;
}

.btn {
  width: 6rem;
  background: #ffffff;
  border: none;
  color: #fff;
  font-size: 1rem;
  text-align: center;
  height: 2rem;
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
  font-size: 0.7rem;
}
.book-intro{
  width: 100vw;
  margin-top: 0.5rem;
  padding-left: 5vw;
  padding-right: 5vw;
  font-size: 1.1rem;
  overflow: auto;
  text-align:justify;
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
    margin-top: 2rem;
}

.chapter-list li {
    padding-top: 1rem;
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
    padding-bottom: 1rem;
}
.hide-chapter {
  position: fixed;
  right: 0;
  top: 0;
  height: 100vh;
  width: 20vw;
}
.long-intro-img {
  width: 100vw;
  height: auto;
}
.bottom-img {
  width: 90vw;
  height: auto;
  margin: 5vw;
}
.bottom-container {
  margin-top: 0.5rem;
}
.book-des {
  margin-top: 0.5rem;
}
.ago {
  font-size: 0.7rem;
}
.comment-head {
	  width: 90vw;
  	margin-top: 0.5rem;
  	margin-left: 5vw;
  	margin-right: 5vw;
  	padding-top: 0.3rem;
  	padding-left: 0.2rem;
  	font-size: 1.1rem;
  	height: 2rem;
  	overflow: auto;
  	text-align: middle;
  	background-color: #E9E5DF;
    color: #73553A;
}
.comment {
    width: 90vw;
    margin-top: 0.5rem;
    margin-left: 5vw;
    margin-right: 5vw;
    padding-top: 0.3rem;
    padding-left: 0.2rem;
    padding-bottom: 0.2rem;
    font-size: 0.8rem;
    border-bottom: 0.2rem solid #E9E5DF;
}
.comment-name {
  color: #00553F;
}
.reply {
  width: 85vw;
    margin-top: 0.3rem;
    margin-left: 5vw;
    margin-right: 5vw;
    padding-left: 0.2rem;
    padding-bottom: 0.2rem;
    font-size: 0.8rem;
    border-bottom: 0.1rem solid #E9E5DF;
}
.post-relpy {
  width: 85vw;
  margin-left: 10vw;
  font-size: 0.8rem;
  color: #00553F;
  margin-top: 0.5rem;
}
.post-name {
  width: 40vw;
  margin-top: 0.5rem;
  margin-left: 10vw;
  border-radius: .4rem;
  margin-bottom: 0.5rem;
}
.post-content {
  width: 85vw;
  height: 4rem;
  overflow: auto;
  margin-left: 10vw;
}
.post-button {
  float: left;
  margin-left: 10vw;
}
.post-button-one {
  width: 4rem;
  margin-top: 0.5rem;
  margin-right: 1rem;
  text-align: center;
  background-color: #00553F;
  color: #FFFFFF;
  border-radius: 0.4rem;
  border: none;
}
</style>
