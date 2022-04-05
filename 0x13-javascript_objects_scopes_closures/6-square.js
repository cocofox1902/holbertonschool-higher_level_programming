#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = c;
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write(char);
      }
      console.log('');
    }
  }
}

module.exports = Square;
