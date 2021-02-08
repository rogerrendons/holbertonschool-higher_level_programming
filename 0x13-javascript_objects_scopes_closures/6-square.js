#!/usr/bin/node
const XSquare = require('./5-square.js');

module.exports = class Square extends XSquare {
    charPrint(C){
    if (C == null){
        C = "X"
    }
    for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
  }
};
