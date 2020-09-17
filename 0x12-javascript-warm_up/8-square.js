#!/usr/bin/node
const times = parseInt(process.argv[2]);
const text = "Missing size"

if (!isNaN(times)) {
  for (let i = 0; i < times; i++) {
    let sqrt = '';
    for (let j = 0; j < times; j++) {
      sqrt += 'X';
    }
    console.log(sqrt);
  }
} else {
  console.log(text);
}
