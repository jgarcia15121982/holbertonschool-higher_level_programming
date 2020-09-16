#!/usr/bin/node


if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('Nan');
}
if (process.argv.length === 4) {
  
  let a = parseInt(process.argv[2]);
  let b = parseInt(process.argv[3]);
  
  function add(a, b) {
    let c = a + b;
    return c;
  }
  console.log(add(a,b));
}


