#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);

request(fullUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    let count = 0;
    const characterNames = [];
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, response, body) => {
        if (!err) {
          const charName = JSON.parse(body).name;
          characterNames.push(charName);
        }
        count++;
        if (count === characters.length) {
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  }
});
