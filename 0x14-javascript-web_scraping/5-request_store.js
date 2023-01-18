#!/usr/bin/node
// Gets the content of a webepage and stores it in a file

const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) { throw err; }
  fs.writeFile(process.argv[3], body, (error) => {
    if (error) { throw error; }
  });
});
