#!/usr/bin/node
exports.converter = function (base) {
  const NUMCONV = function numConv (n) {
    return n.toString(base);
  };
  return NUMCONV;
};
