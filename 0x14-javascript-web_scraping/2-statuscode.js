#!/usr/bin/node

const axios = require('axios').default;

axios
  .get(process.argv[2])
  .then(function (response) {
    console.error('code:', response.status);
  })
  .catch(function (error) {
    console.error('code: ', error.response.status);
  });
