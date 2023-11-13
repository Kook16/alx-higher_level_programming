#!/usr/bin/node

const argv = process.argv;

const len = argv.length;

const startidx = 2;
const endidx = len;

if (len <= 3) {
  console.log(0);
} else {
  const arr = argv.slice(startidx, endidx);
  const newArr = arr.map(Element => parseInt(Element));
  newArr.sort((a, b) => b - a);
  console.log(newArr[1]);
}
