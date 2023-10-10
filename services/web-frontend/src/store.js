import { createStore } from 'vuex';
const store = createStore({
  state: {
    flightSearchFilter: {
      from_country: null,
      to_country: null,
      adult_passengers_count: 1,
      teenager_passengers_count: 0,
      child_passengers_count: 0,
      is_business_class: false,
      departure_date: null,
      back_date: null,
      no_back_ticket: false
    },
    firstGroupPassengersCount: 1,
    secondGroupPassengersCount: 0,
    thirdGroupPassengersCount: 0,
  },
  mutations: {
    setFirstGroupPassengersCount(state, data) {
      state.firstGroupPassengersCount = data;
    },
    setSecondGroupPassengersCount(state, data) {
      state.secondGroupPassengersCount = data;
    },
    setThirdGroupPassengersCount(state, data) {
      state.thirdGroupPassengersCount = data;
    },

    setFlightSearchFilter(state, data) {
      state.flightSearchFilter = data;
    },

  },
  actions: {
    updateFirstGroupPassengersCount({commit}, data) {
      commit('setFirstGroupPassengersCount', data);
    },
    updateUserFullName({commit}, data) {
      commit('setUserFullName', data);
    },
    updateGamePlayersCount({commit}, data) {
      commit('setGamePlayersCount', data);
    },
    updateFieldValues({commit}, data) {
      commit('setFieldValues', data);
    },
    flightSearchFilter({commit}, data) {
      commit('setFlightSearchFilter', data);
    }
  },
  getters: {
    getFlightSearchFilter: state => state.flightSearchFilter,
  }
});

export default store;

