#!/usr/bin/node
// Prints all charcters of a star wars movie

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) { console.log(response.statusCode); throw err; }
  const res = JSON.parse(body).characters;
  res.forEach(element => {
    request(element, (err, response, body) => {
      if (err) { throw err; }
      console.log(JSON.parse(body).name);
    });
  });
});
