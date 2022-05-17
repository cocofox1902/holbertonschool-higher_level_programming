#!/usr/bin/node

const axios = require('axios').default;

axios
  .get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    console.error(response.data.title);
  })
  .catch(function () {
    console.error('error');
  });
