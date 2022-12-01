#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) { console.error(err); }
  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) { console.error(err); }
    const data3 = `${data1.slice(0, -1)}\n${data2.slice(0, -1)}\n`;
    fs.writeFile(process.argv[4], data3, (err) => {
      if (err) throw err;
    });
  });
});
