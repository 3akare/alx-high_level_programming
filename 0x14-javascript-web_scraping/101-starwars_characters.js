#!/usr/bin/node
// Prints all charcters of a star wars movie
const request = require('request');

async function getData (filmId) {
  let filmResponse;
  try {
    filmResponse = await new Promise((resolve, reject) => {
      request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          resolve({ response, body });
        }
      });
    });
    const characters = JSON.parse(filmResponse.body).characters;
    for (const character of characters) {
      const characterResponse = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve({ response, body });
          }
        });
      });
      console.log(JSON.parse(characterResponse.body).name);
    }
  } catch (error) {
    console.log(filmResponse.response.statusCode);
    throw error;
  }
}

getData(process.argv[2]);
