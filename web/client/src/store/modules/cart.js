import shop from '../../api/shop';

// initial state
// shape: [{ id, quantity }]
const state = {
  items: [],
  checkoutStatus: null,
};

// getters
const getters = {
  cartProducts: (store, _, rootState) => store.items.map(({ id, quantity }) => {
    const product = rootState.products.all.find((p) => p.id === id);
    return {
      title: product.title,
      price: product.price,
      quantity,
    };
  }),

  // eslint-disable-next-line max-len
  cartTotalPrice: (_, g) => g.cartProducts.reduce((total, product) => total + product.price * product.quantity, 0),
};

// actions
const actions = {
  checkout({ commit, store }, products) {
    const savedCartItems = [...store.items];
    commit('setCheckoutStatus', null);
    // empty cart
    commit('setCartItems', { items: [] });
    shop.buyProducts(
      products,
      () => commit('setCheckoutStatus', 'successful'),
      () => {
        commit('setCheckoutStatus', 'failed');
        // rollback to the cart saved before sending the request
        commit('setCartItems', { items: savedCartItems });
      },
    );
  },

  addProductToCart({ store, commit }, product) {
    commit('setCheckoutStatus', null);
    if (product.inventory > 0) {
      const cartItem = store.items.find((item) => item.id === product.id);
      if (!cartItem) {
        commit('pushProductToCart', { id: product.id });
      } else {
        commit('incrementItemQuantity', cartItem);
      }
      // remove 1 item from stock
      commit('products/decrementProductInventory', { id: product.id }, { root: true });
    }
  },
};

// mutations
const mutations = {
  pushProductToCart(store, { id }) {
    store.items.push({
      id,
      quantity: 1,
    });
  },

  incrementItemQuantity(store, { id }) {
    const cartItem = store.items.find((item) => item.id === id);
    cartItem.quantity += 1;
  },

  setCartItems(store, { items }) {
    Object.assign(store.items, items);
  },

  setCheckoutStatus(store, status) {
    Object.assign(store.checkoutStatus, status);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
