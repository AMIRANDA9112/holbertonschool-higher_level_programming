#!/usr/bin/node
// computes the number of tasks completed by user id
const rq = require('request');
const url1 = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + url1

rq(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    for (const char of data) {
      rq(char, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          const charName = JSON.parse(body).name;
          console.log(charName);
        }
      });
    }
  }
});
