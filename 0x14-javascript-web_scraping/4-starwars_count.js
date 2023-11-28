#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const results = JSON.parse(body).results;
  for (const filmId in results) {
    const filmChars = results[filmId].characters;
    for (const i in filmChars) {
      if (filmChars[i].includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
