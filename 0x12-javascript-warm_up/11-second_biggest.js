#!/usr/bin/node
const process = require('process');
const myVar = parseInt(process.argv.length);
let x = 0;
if ((myVar <= 3)) {
  console.log(0);
} else {
  const order = process.argv.sort();
  while (x !== myVar) {
    x++;
  }
  x -= 1;
  console.log(order[x - 1]);
}
