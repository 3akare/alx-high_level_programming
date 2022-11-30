#!/usr/bin/node

exports.esrever = function (list) {
  const array = [];
  let i = list.length - 1;
  while (i !== -1) {
    array.push(list[i]);
    i--;
  }
  return (array);
};
