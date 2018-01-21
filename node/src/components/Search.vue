<template>
  <div>
    <div class="search-head">
      <span class="search-icon">
        <Icon type="ios-search-strong"></Icon>
      </span>
      <input type="text" class="search-input" placeholder="输入书名或者作者名" @input="autoComplete" @keyup.enter="fuzzySearch" v-model="searchWord">
      <!--button type="button" class="cancel" @click="$router.push({path:back})">取消</button-->
      <button type="button" class="cancel" @click="$router.push('/bookcat')">取消</button>
    </div>
    <!--只有在没有自动补全与搜索结果时，显示热搜词（优先级最低）-->
    <ul class="search-word" v-if="!autoCompleteList.length && !searchResult.length && !loading">
      <li class="search-hot-word" v-if="searchHotWords" v-for="(searchHotWord, index) in searchHotWords" :key="index" @click="fuzzySearch">{{searchHotWord.word}}
      </li>
    </ul>
    <!--有自动补全数据就显示自动补全（优先级最高）-->
    <ul class="auto-complete-list" v-if="autoCompleteList.length">
      <li v-for="(item, index) in autoCompleteList" :key="index" @click="fuzzySearch">
        <span class="search-result-icon">
          <Icon type="ios-search-strong">  </Icon>
        </span>{{item}}
      </li>
    </ul>
    <pulse-loader :loading="loading" :color="color" :size="size" :margin="margin"></pulse-loader>
    <!--没有自动补全且有搜索结果就显示（优先级中）-->
    <transition name="fade">
      <ul class="search-result" v-if="searchResult.length && !autoCompleteList.length && !loading">
        <li v-for="book in searchResult" :book="book" :key="book._id">
          <div v-if="book.is_book" @click="getBook(book)" class="li-class">
            <img :src="getImgSrc(book)" />
            <div class="book-info">
              <p class="book-title" v-if="book">{{book.title}}</p>
              <p style="line-height:0.6rem;">&nbsp;</p>
              <p class="book-line"></p>
              <p style="line-height:0.6rem;">&nbsp;</p>
              <p class="book-author" v-if="book">{{book.author}}</p>
              <p class="short-intro">{{book.shortIntro}}</p>
              <p class="reader-info">&nbsp;{{book.read_count}}人次阅读</p>
            </div>
          </div>
          <div v-if="!book.is_book" class="li-chapter" @click="getChapter(book)">
            <div class="title">&nbsp;·&nbsp;{{book.title}}</div>
            <div class="title2">&nbsp;&nbsp;&nbsp;{{book.title2}}</div>
          </div>
        </li>
        <!--Booklist v-for="book in searchResult" :book="book" :key="book._id"></Booklist-->
      </ul>
    </transition>
  </div>
</template>

<script>
import api from '../libs/api';
import Booklist from '@/components/Booklist';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

export default {
  name: 'Search',
  components: {
    Booklist,
    PulseLoader
  },
  data() {
    return {
      staticPath: api.staticPath,
      searchWord: '',
      searchHotWords: null,
      autoCompleteList: [],
      searchResult: [],
      loading: false,
      color: '#04b1ff',
      size: '10px',
      margin: '4px',
    }
  },
  computed: {
    back() {
      return this.$store.state.backPath.secPath;
    }
  },
  created() {
    api.getHotWords().then(response => {
      this.searchHotWords = response.data.searchHotWords;
      //只取前10个热词
      this.searchHotWords.length = 10;
    }).
      catch(err => {
        console.log(err);
      })
  },
  watch: {
    'searchWord': function () {
      if (!this.searchWord) {
        this.autoCompleteList = [];
      }
    }
  },
  methods: {
    autoComplete(el) {
      this.searchWord = el.target.value;
      api.autoComplete(el.target.value).then(response => {
        this.autoCompleteList = response.data.keywords;
      }).catch(err => {
        console.log(err);
      })
    },
    /****/
    fuzzySearch(el) {
      let search = el.target.value || el.target.innerText;
      this.searchWord = search;
      this.autoCompleteList = [];
      this.loading = true;
      api.fuzzySearch(search).then(response => {
        this.searchResult = response.data.books;
        this.loading = false;
      }).catch(err => {
        console.log(err);
      })
    },
    getBook(book) {
        // 只记录从不是搜索结果中进入书本详情的路径，不然会出现死循环
        // if(this.$route.path.indexOf('/search') === -1){
        //     this.$store.commit('setPrePath', this.$route.fullPath);
        // }
        this.$store.commit('setTitle',book.title);
        this.$router.push('/book/' + book.book_id);
    },
    getImgSrc(book) {
      console.log(book);
        return this.staticPath + book.cover
    },
    getChapter(chapter) {
      this.$store.commit('setTitle',chapter.book_title);
      this.$router.push('/readbook/' + chapter.book_id + '/' + chapter.chapter_id);
    }
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      // 记录下一个路径为search，但上一个路径不为书本详情的路径
      if (to.path.indexOf('/search') > -1 && from.path.indexOf('/book/') == -1) {
        vm.$store.commit('setSecPath', from.path);
      }
    })
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only
 -->
<style scoped>
.search-head {
  position: fixed;
  left: 0;
  width: 100vw;
  height: 3.5rem;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 0 1rem;
  background: #005390;
}

.search-input {
  width: 100%;
  line-height: 2rem;
  padding-left: 1.8rem;
  border-radius: .4rem;
  border: none;
}

.cancel:focus {
  outline: none;
}

.cancel {
  width: 5rem;
  font-size: 1rem;
  padding: .3rem 0 .3rem 0.8rem;
  color: #fff;
  text-align: center;
  border: none;
  background: #005390;
}

.search-word {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin-top: 4rem;
}

.search-hot-word {
  font-size: 0.8rem;
  padding: 0.2rem 0.6rem;
  border: 1px solid #f2f2f2;
  border-radius: 0.8rem;
  margin-left: 0.5rem;
  margin-bottom: 0.5rem;
}

.search-hot-word:active {
  background: #f2f2f2;
}

.auto-complete-list {
  display: flex;
  flex-direction: column;
  width: 100vw;
  margin-top: 3.5rem;
}

.auto-complete-list li {
  padding-left: 1.5rem;
  line-height: 2.5rem;
  border-bottom: 1px solid #f2f2f2;
}

.auto-complete-list li:active {
  background: #f2f2f2;
}

.search-result {
  display: flex;
  flex-direction: column;
  margin-top: 3.5rem;
  width: 100vw;
  background: #f2f2f2;
}

.search-icon {
  position: absolute;
  left: 1.5rem;
  color: #ccc;
  font-size: 1.2rem;
  line-height: 3.5rem;
}
.search-result-icon{
  font-size: 1.2rem;
  line-height: 2.5rem;
  margin-right : 1rem;
}

img {
  width: 6rem;
  height: 8rem;
  float: left;
  margin: 0.5rem;
}

.li-class {
  margin-top: 0.5rem;
  margin-left: 1rem;
  margin-right: 1rem;
  border-bottom: 1px solid #e6dbdb;
  border-top: 2px solid #66ccff;
  height: 10rem;
}

.li-class:active, .li-class:focus{
  background: #ffffff;
}

.book-info {
  box-sizing: border-box;
  width: 100%;
  height: 6rem;
  padding-left: 7.5rem;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.book-title {
  padding-top: 0.5rem;
  font-weight: bold;
  font-size: 1.1rem;
}

.short-intro {
  padding-top: 0.3rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #655555;
}

.book-author {
  color: #655555;
}

.book-info p {
  margin-top: 0;
  margin-bottom: 0;
  line-height: 1.3rem;
}

.book-line {
  width: 2rem;
  border: 3px solid #005390;
}
.book-author {
  font-size: 0.8rem;
}
.reader-info {
  padding-top: 0.5rem;
}

.title {
    font-size: 1.2rem;
    color: #000000;
}
.title2 {
    font-size: 1rem;
    color: #807d7d;
    margin-bottom: 0.3rem;
}
.li-chapter{
  margin-left: 15vw;
  width: 85vw;
}
</style>
