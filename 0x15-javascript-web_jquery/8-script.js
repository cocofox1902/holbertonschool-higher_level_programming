window.$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const i in data.results) {
    window.$('#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
