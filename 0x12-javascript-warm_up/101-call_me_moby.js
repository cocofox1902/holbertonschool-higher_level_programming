#!/usr/bin/node

exports.callMeMoby = function (x, fonc) {
  for (let i = 0; i < x; i++) {
    fonc(i);
  }
};
