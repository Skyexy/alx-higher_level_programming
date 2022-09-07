#!/usr/bin/node
module.exports = class Rectangle {
<<<<<<< HEAD
  constructor (w, h) {
    if (w < 1 || h < 1 || !Number.isInteger(w) || !Number.isInteger(h)) {
      const objectA = {};
    } else {
=======
  constructor(w, h) {
    if (w < 1 || h < 1 || !Number.isInteger(w) || !Number.isInteger(h)){
      objectA = {};
    }
    else {
>>>>>>> efeca1ddf88eb9b64da8542391a364eb8edb5729
      this.width = w;
      this.height = h;
    }
  }
};
