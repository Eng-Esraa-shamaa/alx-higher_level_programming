#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  const last = list.length - 1;
  for (let i = last; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
