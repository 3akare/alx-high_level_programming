#!/usr/bin/node
// print the number of movies where the character "Wedge Antilles" is present

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) { throw err; }
  const res = JSON.parse(body).results;
  let count = 0;
  res.forEach(element => {
    element.characters.forEach(element2 => {
      if (parseInt(element2.slice(-3, -1)) === 18) { count++; }
    });
  });
  console.log(count);
});
