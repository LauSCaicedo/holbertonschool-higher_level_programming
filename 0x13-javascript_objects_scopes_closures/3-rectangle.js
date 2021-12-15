#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let z;
    for (z = 0; z < this.height; z++) {
      console.log('X'.repeat(this.width));
    }
  }
};
