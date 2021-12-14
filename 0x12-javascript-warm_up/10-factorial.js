#!/usr/bin/node
const process = require('process');
const myVar = parseInt(process.argv[2]);

function myFact (n) {
  if (isNaN(n) || (n === 1)) {
    return (1);
  } else {
    return (n * myFact(n - 1));
  }
}
result = myFact(myVar);
console.log(result);
