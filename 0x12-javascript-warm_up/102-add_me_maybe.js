#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let n = number + 1;
  theFunction(n);
};
