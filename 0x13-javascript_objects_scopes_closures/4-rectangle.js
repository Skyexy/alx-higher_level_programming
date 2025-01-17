#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const si = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(si.repeat(this.width));
    }
  }

  rotate () {
    const f = this.width;
    this.width = this.height;
    this.height = f;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
