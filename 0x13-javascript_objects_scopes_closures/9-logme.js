#!/usr/bin/node

let nb = 0;
exports.logMe = function (item) {
  console.log(`${nb}: ${item}`);
  nb++;
};
