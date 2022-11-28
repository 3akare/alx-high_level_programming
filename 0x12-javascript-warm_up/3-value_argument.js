#!/usr/bin/node

let index = 0;

while (process.argv[index]) {
  if (index === 2) {
    console.log(process.argv[index]);
  }
  index++;
}
