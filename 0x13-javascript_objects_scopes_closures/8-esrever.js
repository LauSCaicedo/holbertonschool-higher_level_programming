#!/usr/bin/node
exports.esrever = function (list) {
  const x = [...list].map(list.pop, list);
  return x;
};
