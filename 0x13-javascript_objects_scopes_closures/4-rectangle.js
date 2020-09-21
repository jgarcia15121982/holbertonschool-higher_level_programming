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

  rotate () {
    let w1 = 0;
    let h1 = 0;
    w1 = this.width;
    h1 = this.height;
    this.width = h1;
    this.height = w1;
  }

  double () {
    let w1 = 0;
    let h1 = 0;
    w1 = this.width;
    h1 = this.height;
    this.width = w1 * 2;
    this.height = h1 * 2;
  }
}
module.exports = Rectangle;
