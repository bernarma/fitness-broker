import shop from '../../api/shop';

// initial state
const state = {
  all: [],
};

// getters
const getters = {};

// actions
const actions = {
  getAllProducts({ commit }) {
    shop.getProducts((products) => {
      commit('setProducts', products);
    });
  },
};

// mutations
const mutations = {
  setProducts(store, products) {
    Object.assign(store.all, products);
  },

  decrementProductInventory(store, { id }) {
    const product = store.all.find((p) => p.id === id);
    product.inventory -= 1;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
