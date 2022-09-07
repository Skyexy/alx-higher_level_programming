#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square {
  constructor (size) {
    super(size);
  }
  charPrint(c) {
    if (c) {
      for (let i = 0; i < size; i++) {
        console.log(c.repeat(size));
      }
    }
    else {
      const si = 'X';
      for (let i = 0; i < args; i++) {
        console.log(si.repeat(args));
      }
    }
  }
};
