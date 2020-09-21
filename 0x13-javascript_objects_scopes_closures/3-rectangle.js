#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let txt = '';
    let i, j;
    for (i = 0; i < this.width; i++) {
      txt += 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(txt);
    }
  }
}
module.exports = Rectangle;
