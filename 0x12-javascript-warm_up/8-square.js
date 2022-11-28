#!/usr/bin/node
const array = [];
if (isNaN(process.argv[2])) { console.log('Missing number of occurrences'); } else {
  const number = parseInt(process.argv[2]);
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) { array.push('X'); }
    console.log(array.join(' '));
    array.length = 0;
  }
}
