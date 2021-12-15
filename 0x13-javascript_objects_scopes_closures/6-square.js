#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      let j;
      for (j = 0; j < this.height; j++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      let z;
      for (z = 0; z < this.height; z++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
