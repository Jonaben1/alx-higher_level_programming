#!/usr/bin/node
exports.esrever = function (list) {
  const co = [];
  for (let x = list.length; x > 0; x--) {
    co.push(list[x - 1]);
  }
  return co;
};
