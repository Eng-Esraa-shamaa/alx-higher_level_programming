#!/usr/bin/node
const dictionary = require('./101-data').dict;
const newD = {};
for (const i in dictionary) {
  if (newD[dictionary[i]] === undefined) {
    newD[dictionary[i]] = [];
  }
  newD[dictionary[i]].push(i);
}
console.log(newD);
