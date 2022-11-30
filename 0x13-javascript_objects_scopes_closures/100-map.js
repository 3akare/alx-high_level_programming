#!/usr/bin/node

const list = require('./100-data.js').list;
const newList = list.map(indexFunc);
function indexFunc (num) {
  return (num * list.indexOf(num));
}

console.log(list);
console.log(newList);
