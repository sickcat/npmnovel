<template>
  <div>
    <pulse-loader :loading="loading" :color="color" :size="size" :margin="margin"></pulse-loader>
    <div v-show="!loading">

      <!-- bookshelf list -->
      <ul class="book-shelf">
        <v-touch tag="li" class="book-list-wrap" v-for="(book, index) in books" :key="index" @swipeleft="showDelBookBtn" @swiperight="hideDelBookBtn">
          <v-touch class="book-list" @tap="gotobook(book)">
            <img :src="getImgSrc(book)" />
            <div class="info">
              <p class="title">{{book.title}}</p>
              <p class="updated">更新时间：{{book.updated | ago}}</p>
              <p class="updated">最后章节：{{book.lastChapter}}</p>
              <v-touch class="continue" @tap="readbook(book)">续看</v-touch>
            </div>
            <v-touch class="del-book-btn" @tap="delBook($event,index)">删除</v-touch>
          </v-touch>
        </v-touch>
        <v-touch tag="li" class="book-list-wrap">
        <button type="button" class="add-book" @click="$router.push('/bookcat')">添加书籍+</button>
        </v-touch>
      </ul>
      <!--div class="book-div">
         <v-touch tag="div" class="book-list-div" v-for="(book, index) in books" :key="index" @swipeleft="showDelBookBtn" @swiperight="hideDelBookBtn">
          <v-touch class="book-list" @tap="readbook(book)">
            <img :src="getImgSrc(book)" />
            <div class="info">
              <p class="title">{{book.title}}</p>
              <p class="updated">{{book.updated | ago}}：{{book.lastChapter}}</p>
            </div>
            <v-touch class="del-book-btn" @tap="delBook($event,index)">删除</v-touch>
          </v-touch>
        </v-touch>
      </div-->

    </div>
  </div>
</template>

<script>
import api from '../libs/api'
import moment from 'moment'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

moment.locale('zh-cn');
export default {
  name: 'Bookshelf',
  components:{
    PulseLoader
  },
  data() {
    return {
      books: [],
      loading: true,
      color: '#04b1ff',
      size: '10px',
      margin: '4px',
      staticPath: api.staticPath,
    }
  },
  filters: {
    /**
     * 使用moment格式化时间
     */
    ago(time) {
      return moment(time).fromNow();
    }
  },
  created() {
    if(!this.parseLocalShelfData()){
      this.loading = false;
    } else{
      this.getBookUpdate();
    }
    if(this.$route.query.user_id) {
      console.log(this.$route.query.user_id);
      this.$store.commit('setUserId',this.$route.query.user_id);
    } else {
      console.log("default");
    }
  },
  methods: {
    /**
     * 格式化locastorage数据
     */
    parseLocalShelfData() {
      return JSON.parse(window.localStorage.getItem('followBookList'));
    },
    /**
     * 返回追更新的书本id
     */
    getBookList() {
      let localShelf = this.parseLocalShelfData();
      let bookListArray = [];
      for (let bookId in localShelf) {
        bookListArray.push(bookId);
      }
      return bookListArray;
    },
    getBookUpdate() {
      // todo 在es6中this的指向待优化
      let localShelf,
        _that = this;
      _that.books = [];
      this.getBookList()
      api.getUpdate(this.getBookList()).then(response => {
        localShelf = this.parseLocalShelfData();
        response.data.forEach((book, index) => {
          Object.assign(book, localShelf[book._id]);
          _that.books.push(book);
        });
        this.loading = false;
      }).catch(err => {
        console.log(err);
        this.loading = false;
      })
    },
    /**
     * 获取封边静态路径
     */
    getImgSrc(book) {
      if (book.cover[0] == "/")
        book.cover = book.cover.substr(1);
      var a = this.staticPath + book.cover;
      return a;
    },
    /**
     * 设置头部文字
     */
    changeHeadText() {
      this.$store.commit('setHeadText', '我的书架');
    },
    readbook(book) {
      this.$store.commit('setTitle',book.title);
      this.$store.commit('setReadBook', book);
      this.$router.push('/readbook/' + book._id);
    },
    gotobook(book) {
      this.$router.push('/book/' + book._id);
    },
    showDelBookBtn(e) {
      let target = e.target.parentElement;
      while (target.className !== 'book-list') {
        target = target.parentElement;
      }
      target.style.left = '-44vw';
    },
    hideDelBookBtn(e) {
      let target = e.target.parentElement;
      while (target.className !== 'book-list') {
        target = target.parentElement;
      }
      target.style.left = '0';
    },
    delBook($event, index) {
      let storage = window.localStorage;
      let localShelf = JSON.parse(storage.getItem('followBookList')) ? JSON.parse(storage.getItem('followBookList')) : {};
      //删除该书籍在本地的缓存记录
      delete localShelf[this.books[index]._id];
      this.books.splice(index, 1);
      //重新保存
      storage.setItem("followBookList", JSON.stringify(localShelf));
    }
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.changeHeadText();
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.add-book {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 0.6rem 2rem;
  color: #fff;
  background: #04b1ff;
  border: none;
  border-radius: .2rem;
  font-size: 1rem;
}

.add-book:focus {
  outline: none;
}

.book-shelf {
  z-index: 0;
  position: absolute;
  left: 0vw;
  width: 100vw;
  overflow: hidden;
  box-sizing: border-box;
  padding: 0.5rem 0 0 1rem;
}

.book-list-wrap {
  position: relative;
  height: 7rem;
  margin-bottom: .5rem;
}

.book-list {
  position: absolute;
  left: 0;
  width: 140vw;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: .2rem;
}

.book-list img {
  width: 5em;
  height: 7rem;
  float: left;
  margin-right: .4rem;
}

.info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-sizing: border-box;
  width: 100%;
  height: 7rem;
  margin-left: .6rem;
  border-bottom: 2px solid #f2f2f2;
  padding-bottom: 1rem;
}

.info p {
  margin-top: .2rem;
  margin-bottom: .2rem;
}

.updated {
  color: #6d6666;
  font-size: .8rem;
}

.del-book-btn {
  color: #fff;
  background: red;
  width: 40vw;
  line-height: 7rem;
  text-align: center;
}

.book-div {
  float: left;
}
.book-list-dev {
  float: left;
}
.continue {
  width: 4rem;
  line-height: 1.8rem;
  font-size: 1rem;
  background: #04b1ff;
  text-align: center;
  border-radius: 4px;
  color: #ffffff;
}

</style>
