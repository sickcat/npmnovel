// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import VueTouch from 'vue-touch'
import router from './router'
import Ajax from './libs/ajax'
import store from './store'
import iView from 'iview'
import 'iview/dist/styles/iview.css'    // 使用 CSS
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'
import vuescroll from 'vue-scroll'
import VueProgressBar from 'vue-progressbar'
import 'jquery'

const options = {
  color: '#bffaf3',
  failedColor: '#874b4b',
  thickness: '5px',
  transition: {
    speed: '0.2s',
    opacity: '0.6s',
    termination: 300
  },
  autoRevert: true,
  location: 'left',
  inverse: false
}
Vue.use(VueProgressBar, options)

Vue.use(vuescroll)
VueTouch.config.swipe = {
  direction: 'horizontal'
};
VueTouch.registerCustomEvent('doubletap', {
  type: 'tap',
  taps: 2
})
Vue.use(VueTouch, {name: 'v-touch'})
Vue.use(iView);
Vue.config.productionTip = false;
Vue.use(Ajax, {
  baseURL: 'http://localhost:8080' //BM: api address?
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App
  }
});
//Disable context menu
document.addEventListener('contextmenu', event => {
  event.preventDefault();
  event.stopPropagation();
});
//Disable double click selection
//document.addEventListener('mousedown', e => {
//  e.preventDefault();
//})