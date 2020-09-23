#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getData (url) {
  request(url, async function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      const data = JSON.parse(body).characters;
      for (const char of data) {
        const chars = await getPeople(char);
        console.log(chars);
      }
    }
  });
}

function getPeople (char) {
  return new Promise((resolve, reject) => {
    request(char,
      function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
  });
}

getData(url);
