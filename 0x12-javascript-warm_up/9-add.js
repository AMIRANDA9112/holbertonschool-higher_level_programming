#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const n = Number(process.argv[2]);
const n1 = Number(process.argv[3]);

add(n, n1);
