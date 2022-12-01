#!/usr/bin/node

const dict = require('./100-data').dict;
const dictList = Object.values(dict);
const newDict = {};
dictList.forEach(element => {
  newDict[element] = [];
});

for (const [key, value] of Object.entries(dict)) {
  newDict[value].push(key);
}

console.log(newDict);
