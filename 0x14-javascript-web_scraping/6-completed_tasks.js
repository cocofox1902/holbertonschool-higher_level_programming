#!/usr/bin/node

const axios = require('axios');

const List = {};
let value;
axios
  .get(process.argv[2])
  .then((res) => {
    for ([, value] of Object.entries(res.data)) {
      if (value.completed === true) {
        if (List[value.userId] === undefined) {
          List[value.userId] = 0;
        }
        List[value.userId] += 1;
      }
    }
    console.log(List);
  })
  .catch((err) => {
    console.error(err);
  });
