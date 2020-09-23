#!/usr/bin/node
const fileSyste = require('fs');
fileSystes.readFile(process.argv[2], 'utf8', function (err, contents) {
  if (contents === undefined) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
