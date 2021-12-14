#!/usr/bin/node
const process = require('process');
const myVar = parseInt(process.argv[2]);
const myVar2 = parseInt(process.argv[3]);

function add(a, b) {
  return (a + b);
}
console.log(add(myVar, myVar2));
