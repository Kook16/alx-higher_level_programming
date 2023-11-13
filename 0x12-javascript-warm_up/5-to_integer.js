#!/usr/bin/node

const argv = process.argv;

const result = parseInt(argv[2]);

if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + result);
}
