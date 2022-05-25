window.$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  window.$('#hello').append(data.hello);
});
