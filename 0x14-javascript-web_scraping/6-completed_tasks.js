#!/usr/bin/node
// Computes the number of tasks complted by userid

const request = require('request');

const dict = {};
request(process.argv[2], (err, response, body) => {
  if (err) { throw err; }
  const res = JSON.parse(body);
  res.forEach(element => {
    if (element.completed === true) {
      if (element.userId in dict === false) { dict[element.userId] = 0; }
      dict[element.userId] = parseInt(dict[element.userId]) + 1;
    }
  });
  console.log(dict);
});
