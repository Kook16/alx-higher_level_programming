#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const ele of list) {
    if (searchElement === ele) {
      ++i;
    }
  }
  return i;
};
