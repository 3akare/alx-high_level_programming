#!/usr/bin/node
// prints the content of a file
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.log(err);
  } else { console.log(data1); }
});
