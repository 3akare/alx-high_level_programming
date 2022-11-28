#!/usr/bin/node

let index = 0;
if (process.argv.length <= 2) { console.log('No argument'); } else {
  process.argv.forEach(element => {
    if (index === 2) {
      console.log(element);
    }
    index++;
  });
}
