#!/usr/bin/node
const num = require('./100-data').list;
console.log(num);
const newList = num.map(function (numb, index) {
  return (numb * index);
});

console.log(newList);
