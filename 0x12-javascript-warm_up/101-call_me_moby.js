#!/usr/bin/node

exports.callMeMoby = function(x, fonc) {
  for (var i = 0; i < x; i++) {
	fonc(i);
  }
};
