#!/usr/bin/node

const axios = require('axios');

axios
  .get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(async (res) => {
    for (const characters of res.data.characters) {
      await axios.get(characters).then((res) => {
        console.log(res.data.name);
      });
    }
  })
  .catch((err) => {
    console.log(`code: ${err.response.status}`);
  });
