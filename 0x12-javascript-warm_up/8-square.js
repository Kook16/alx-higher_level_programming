#!/usr/bin/node

// script that prints a square

const size = process.argv[2];

if (!size) { console.log('Missing size'); } else if (size !== NaN && size > 0) {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
