#!/usr/bin/node
/*
   print a square
*/
const argv = process.argv;
const number = argv.length;

if (number <= 3) {
  console.log('0');
} else {
  const se = argv.sort(function (a, b) { return (b - a);});
  console.log(se[3]);}
