#!/usr/bin/node
const rq = require('request');

rq(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
