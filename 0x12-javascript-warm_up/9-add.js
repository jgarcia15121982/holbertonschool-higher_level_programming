#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('Nan');
}
if (process.argv.length === 4) {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  console.log(add(a, b));
}

function add (a, b) {
  return a + b;
}
