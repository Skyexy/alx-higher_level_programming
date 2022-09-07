#!/usr/bin/node
const me = require('./5-square');
module.exports = class Square extends me {
  constructor (size) {
    super(size);
    this.size = size;
  }
  charPrint(c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
    else {
      const si = 'X';
      for (let i = 0; i < this.width; i++) {
        console.log(si.repeat(this.width));
      }
    }
  }
};
