#!/usr/bin/node

const argv = process.argv;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(a + b);
}
