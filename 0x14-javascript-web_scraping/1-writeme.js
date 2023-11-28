#!/usr/bin/node

const fs = require('fs');
const FileName = process.argv[2];
const content = process.argv[3];

fs.writeFile(FileName, content, function (err) {
  if (err) {
    console.log(err);
  }
});
