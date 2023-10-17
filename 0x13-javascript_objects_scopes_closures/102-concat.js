#!/usr/bin/node
const file = require('fs');
const args = process.argv.slice(2);
const argA = file.readFileSync(args[0]).toString();
const argB = file.readFileSync(args[1]).toString();
file.writeFileSync('./' + args[2], argA + argB);
