#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.readFile(process.argv[2], 'utf8', function (err, contents) {
  if (contents === undefined) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
