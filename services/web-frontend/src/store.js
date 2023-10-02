import { createStore } from 'vuex';
const store = createStore({
  state: {
    GamePlayersCount: 2,
    UserId: null,
    UserFullName: null,
    fieldValues: []
  },
  mutations: {
    setUserId(state, data) {
      state.UserId = data;
    },
    setUserFullName(state, data) {
      state.UserFullName = data;
    },
    setGamePlayersCount(state, data) {
      state.GamePlayersCount = data;
    },
    setFieldValues(state, data) {
      state.fieldValues = data;
    },
  },
  actions: {
    updateUserId({commit}, data) {
      commit('setUserId', data);
    },
    updateUserFullName({commit}, data) {
      commit('setUserFullName', data);
    },
    updateGamePlayersCount({commit}, data) {
      commit('setGamePlayersCount', data);
    },
    updateFieldValues({commit}, data) {
      commit('setFieldValues', data);
    }
  },
  getters: {
    getUserId: state => state.UserId,
    getUserFullName: state => state.UserFullName,
    getGamePlayersCount: state => state.GamePlayersCount,
    getFieldValues: state => state.fieldValues
  }
});

export default store;

