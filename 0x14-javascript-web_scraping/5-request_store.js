#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

axios
  .get(process.argv[2])
  .then((res) => {
    if (res.status === 200) {
      fs.writeFile(`./${process.argv[3]}`, res.data, { flag: 'w+' }, (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  })
  .catch((err) => {
    console.error(err);
  });
