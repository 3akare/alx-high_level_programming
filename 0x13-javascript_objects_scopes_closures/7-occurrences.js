#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(element => {
    if (element === searchElement) { i++; }
  });
  return (i);
};
