window.$().ready(function () {
  window.$('#btn_translate').click(function () {
    window.$.get('https://fourtonfish.com/hellosalut/?lang=' + (window.$('#language_code')).val(), function (data) {
      window.$('#hello').text(data.hello);
    });
  });
  window.$('#language_code').keypress(function (event) {
    if (event.which === 13) {
      console.log('enter');
      window.$.get('https://fourtonfish.com/hellosalut/?lang=' + (window.$('#language_code')).val(), function (data) {
        window.$('#hello').text(data.hello);
      });
    }
  });
});
