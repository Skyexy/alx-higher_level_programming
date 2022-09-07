#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 || h > 1 || Number.isInteger(w) || Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }
}
