#!/usr/bin/node

// script that prints a square

const size = process.argv[2];

if (!isNaN(size)) {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
} else {
    console.log('Missing size');
}
