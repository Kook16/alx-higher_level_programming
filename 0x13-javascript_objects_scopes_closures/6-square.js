#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) { super.print(); } else {
      for (let i = 0; i < this.size; i++) {
        let print = '';
        for (let j = 0; j < this.size; j++) {
          print += c;
          console.log(print);
        }
      }
    }
  }
}

module.exports = Square;
