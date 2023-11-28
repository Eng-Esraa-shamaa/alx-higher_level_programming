#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);

request(fullUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    let count = 0;
    const characterNames = [];
    const printCharacters = () => {
      characters.forEach((characterUrl, index) => {
        request(characterUrl, (err, response, body) => {
          if (!err) {
            const charName = JSON.parse(body).name;
            characterNames[index] = charName;
            count++;
            if (count === characters.length) {
              characterNames.forEach((actor) => {
                console.log(actor);
              });
            }
          } else {
            console.error(err);
          }
        });
      });
    };

    printCharacters();
  }
});
