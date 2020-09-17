#!/usr/bin/node

const argv = process.argv;
const numberArgv = argv.length;

if (numberArgv <= 3) {
  console.log('0');
} else {
  const secondb = argv.sort(function (a, b) { return (b - a); });
  console.log(secondb[3]);
}
