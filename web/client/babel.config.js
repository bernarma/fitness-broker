module.exports = function babel(api) {
  api.cache(true);

  const presets = ['@vue/cli-plugin-babel/preset'];
  const plugins = [];

  return {
    presets,
    plugins,
  };
};
