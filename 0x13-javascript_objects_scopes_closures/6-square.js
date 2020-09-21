#!/usr/bin/node
const SqBase = require('./5-square.js');

class Square extends SqBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let txt = '';
    let i, j;
    for (i = 0; i < this.width; i++) {
      txt += c;
    }
    for (j = 0; j < this.width; j++) {
      console.log(txt);
    }
  }
}

module.exports = Square;
