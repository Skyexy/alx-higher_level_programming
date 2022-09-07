#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 1 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    const si = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(si.repeat(this.width));
    }
  }
}
