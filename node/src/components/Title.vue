<template>
  <div class="flash">
    <div>flash</div>
    <img src="/static/png/title.png">
  </div>
</template>

<script>
import Topbar from './Topbar'
import api from '../libs/api'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import moment from 'moment'

export default {
  name: 'Title',
  components: {
    Topbar,
    PulseLoader
  },
  data() {
    return {
    }
  },
  filters: {
  },
  computed: {
  },
  created() {
    console.log("aaa");
  },
  beforeRouteEnter(to, from, next) {  
  },
  methods: {
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.flash {
  height: 100vh;
  width: 100vw;
}

</style>
