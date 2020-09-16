#!/usr/bin/node
function add (a, b) {
  return a + b;
}

if (!process.argv[3] || isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('Nan');
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  console.log(add(a, b));
}
