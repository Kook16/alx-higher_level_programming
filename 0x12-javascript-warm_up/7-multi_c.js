#!/usr/bin/node
const times = process.argv[2];

if (!isNaN(times)) {
  let i = 0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurences');
}
