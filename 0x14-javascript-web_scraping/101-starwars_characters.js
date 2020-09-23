#!/usr/bin/node
// computes the number of tasks completed by user id
const rq = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

rq(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let result = [];
    result = (JSON.parse(body).characters);
    for (let element of result) {
      rq(element, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
