#!/usr/bin/node

const argv = process.argv;
const numberArgv = argv.length;

if (numberArgv <= 3) {
  console.log('0');
} else {
  const se = argv.sort(function (a, b) { return (b - a); });
  console.log(se[3]);
}
