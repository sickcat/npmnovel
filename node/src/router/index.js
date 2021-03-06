import Vue from 'vue'
import Router from 'vue-router'
import Bookshelf from '@/components/Bookshelf'
import Bookcat from '@/components/Bookcat'
import Rank from '@/components/Rank'
import Overview from '@/components/Overview'
import Ranklist from '@/components/Ranklist'
import RanklistDetail from '@/components/RanklistDetail'
import Book from '@/components/Book'
import ReadBook from '@/components/ReadBook'
import Search from '@/components/Search'
import BookcatDetail from '@/components/BookcatDetail'
import Title from '@/components/Title'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/bookcat/detail',
      name: 'bookcatDetail',
      component: BookcatDetail
    }, {
      path: '/readbook/:bookId',
      name: 'readbook',
      component: ReadBook
    }, {
      path: '/readbook/:bookId/:chapterId',
      name: 'readbook',
      component: ReadBook
    }, {
      path: '/book/:bookId',
      name: 'book',
      component: Book
    }, {
      path: '/search',
      name: 'search',
      component: Search
    }, {
      path: 'searchresult'
    }, {
      path: '/flash',
      name: 'flash',
      component: Title,
    }, {
      path: '/',
      component: Overview,
      redirect: '/bookshelf',
      children: [{
        path: '/bookshelf',
        name: 'bookshelf',
        component: Bookshelf
      }, {
        path: '/bookcat',
        name: 'bookcat',
        component: BookcatDetail
      }]
    },
  ]
})
