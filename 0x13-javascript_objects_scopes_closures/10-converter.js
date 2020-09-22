#!/usr/bin/node
// convert number base
exports.converter = function (base) {
  function toBase (value) {
    return value.toString(base);
  }
  return toBase;
};
