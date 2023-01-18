#!/usr/bin/node
// display status code from a GET request

const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) { throw err; }
  console.log(`code: ${response.statusCode}`);
});
