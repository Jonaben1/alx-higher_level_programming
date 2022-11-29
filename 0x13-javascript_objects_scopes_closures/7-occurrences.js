#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let co = 0;
  for (const x in list) {
    if (list[x] === searchElement) {
      co += 1;
    }
  }
  return co;
};
