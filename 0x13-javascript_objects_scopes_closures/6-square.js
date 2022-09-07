#!/usr/bin/node
const me = require('./5-square');
module.exports = class Square extends me {
  constructor (size) {
    super(size);
    this.size = size;
  }
  charPrint(c) {
    if (c) {
      for (let i = 0; i < this.h; i++) {
        console.log(c.repeat(this.h));
      }
    }
    else {
      const si = 'X';
      for (let i = 0; i < this.h; i++) {
        console.log(si.repeat(this.h));
      }
    }
  }
};
