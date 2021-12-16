#!/usr/bin/node
const process = require('process');
const myVar = process.argv.length;
const order = process.argv.sort((a, b) => (a - b));
let x = 0;
if (myVar <= 3) {
  console.log(0);
} else {
  while (x !== myVar) {
    x++;
  }
  console.log(order[x - 2]);
}
