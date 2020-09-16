#!/usr/bin/node
let i;
let txt = '';
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    txt += 'X';
  }
  for (i = 0; i < process.argv[2]; i++) {
    console.log(txt);
  }
}
