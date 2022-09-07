#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w < 1 || h < 1 || !isNaN(w) || !isNaN(h)){
      var objectA = {};
    }
    else {
      this.width = w;
      this.height = h;
    }
  }
}
