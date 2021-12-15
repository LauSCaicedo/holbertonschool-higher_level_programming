#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      let z;
      for (z = 0; z < this.height; z++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
