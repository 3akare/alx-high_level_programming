#!/usr/bin/node

let i = 2;
const array = [];
let temp = 0;
try {
  while (process.argv[i]) {
    array.push(parseInt(process.argv[i]));
    i++;
  }

  while (i !== 0) {
    for (let index = 0; index < array.length; index++) {
      if (array[index] - array[index + 1] > 0) {
        temp = array[index];
        array[index] = array[index + 1];
        array[index + 1] = temp;
      }
    }
    i--;
  }
} catch (error) {
  console.log('error found');
}

if (array.length <= 1) {
  console.log(0);
} else {
  console.log(array[array.length - 2]);
}
