#!/usr/bin/node
const process = require('process');
const myVar = process.argv.length;
const order = process.argv.sort();
let x = 0;
if (myVar <= 3) {
  console.log(0);
} else {
  while (x !== myVar) {
    x++;
  }
  x -= 1;
  console.log(order[x - 1]);
}
