#!/usr/bin/node
const times = process.argv[2];

if (!times) { console.log('Missing number of occurrences'); } else if (!isNaN(times) && times > 0) {
  let i = 0;
  while (i < times) {
    console.log('C is fin');
    i++;
  }
}
