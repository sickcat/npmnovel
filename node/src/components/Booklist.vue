<template>
  <li @click="getBook()">
    <img :src="getImgSrc()" />
    <!--div class="book-info">
      <p class="book-title">{{book.title}}</p>
      <p class="book-author">{{book.author}}  {{book.cat}}</p>
      <p class="short-intro">{{book.shortIntro}}</p>
      <p class="reader-info">{{book.read_count}}人次阅读</p>
    </div-->
    <div class="book-info">
      <p class="book-title" v-if="book">{{book.title}}</p>
      <p style="line-height:0.6rem;">&nbsp;</p>
      <p class="book-line"></p>
      <p style="line-height:0.6rem;">&nbsp;</p>
      <p class="book-author" v-if="book">{{book.author}}</p>
      <p class="short-intro">{{book.shortIntro}}</p>
      <p class="reader-info">&nbsp;{{book.read_count}}人次阅读</p>
    </div>
  </li>
</template>

<script>
import api from '../libs/api'
  export default {
    name: 'Bookslist',
    data() {
      return {
        staticPath: api.staticPath,
      }
    },
    props: ['book'],
    computed: {
      latelyFollower() {
        return 100
      }
    },
    methods: {
      getImgSrc() {
        return this.staticPath + this.book.cover
      },
      getBook() {
        // 只记录从不是搜索结果中进入书本详情的路径，不然会出现死循环
        // if(this.$route.path.indexOf('/search') === -1){
        //     this.$store.commit('setPrePath', this.$route.fullPath);
        // } 
        this.$router.push('/book/' + this.book._id);
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  img {
    width: 6rem;
    height: 8rem;
    float: left;
    margin: 0.5rem;
  }
  
  li {
    margin-left: 1rem;
    margin-right: 1rem;
    border-bottom: 1px solid #e6dbdb;
    height: 10rem;
  }
  
  li:active, li:focus{
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

</style>
