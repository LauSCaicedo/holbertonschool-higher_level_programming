#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x;
  let cont = 0;
  for (x = 0; x in list; x++) {
    if (list[x] === searchElement) {
      cont += 1;
    }
  }
  return cont;
};
