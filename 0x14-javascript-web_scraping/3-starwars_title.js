#!/usr/bin/node
// prints the title of a star wars movie where the episode number matches a given integer

// eslint-disable-next-line no-unused-vars
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) { console.log(response.statusCode); throw err; }
  console.log(JSON.parse(body).title);
});
