#!/usr/bin/node
// Revers sort list
exports.esrever = function (list) {
  const reversed = [];
  while (list.length) {
    reversed.push(list.pop());
  }
  return reversed;
};
