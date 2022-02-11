import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    session_name: ''
  },
  mutations: {
    name (state, sessionName) {
      this.state.session_name = sessionName
    }
  }
})
