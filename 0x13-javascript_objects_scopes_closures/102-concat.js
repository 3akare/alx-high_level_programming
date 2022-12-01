#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) { data1 = ''; }
  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) { data2 = ''; }
    const data3 = `${data1}${data2}`;
    fs.writeFile(process.argv[4], data3, (err) => {
      if (err) throw err;
    });
  });
});
