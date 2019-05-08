// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuex from 'vuex'

Vue.use(Vuex)

var data = [
  { id: 1, title: '标题1', content: '内容1' },
  { id: 2, title: '标题2', content: '内容2' },
  { id: 3, title: '标题3', content: '内容3' },
  { id: 4, title: '标题4', content: '内容4' },
]

const store = new Vuex.Store({
  state: {
    alllist: [],
    note: {
      title: '',
      content: '',
      // markdown: '',
    }
  },
  mutations: {
    GETALLLIST(state, newdata) {
      state.alllist = newdata;
    },
    ADDONENOTE(state, newdata) {
      state.alllist = newdata;
    },
  },
  actions: {
    getAllList(context) {
      context.commit('GETALLLIST', data)
      // axios.get('url').then(function (response) { 
      //   console.log(response);
      // }).catch(function (error) { 
      //   console.log(error);
      // });
    },
    addOneNote(context, json) {
      data.push(json)
      context.commit('ADDONENOTE', data)
    }
  }
});

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
