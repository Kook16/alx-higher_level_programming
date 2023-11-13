#!/usr/bin/node

const idx = parseInt(process.argv[2]);

if (isNaN(idx)) {
  console.log('Missing number of occurrences');
} if (idx > 0) {
  for (let i = 0; i < idx; i++) {
    console.log('C is fun');
  }
}
