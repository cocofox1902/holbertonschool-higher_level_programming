window.$().ready(function () {
  window.$('#btn_translate').click(function () {
    window.$.get('https://fourtonfish.com/hellosalut/?lang=' + (window.$('#language_code')).val(), function (data) {
      window.$('#hello').text(data.hello);
    });
  });
});
