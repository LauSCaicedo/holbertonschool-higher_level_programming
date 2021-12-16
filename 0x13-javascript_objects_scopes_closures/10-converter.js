#!/usr/bin/node
exports.converter = function (base) {
  function numConv (n) {
    return n.toString(base);
  }
  return numConv;
};
