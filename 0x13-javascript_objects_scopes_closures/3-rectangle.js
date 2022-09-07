#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || !Number.isInteger(w) || !Number.isInteger(h)) {
      let obj = {};
    }
    else {
      this.width = w;
      this.height = h;
    }
    print() {
      for (let i = 0; i < h; i++) {
      console.log(si.repeat(w));
      }
    }
  }
