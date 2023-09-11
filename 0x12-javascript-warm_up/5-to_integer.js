#!/usr/bin/node

// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:

const value = parseInt(process.argv[2]);
let message;

if (value === NaN) { console.log('Not a number'); } else { console.log(`My number: ${value}`); }

process.argv.forEach((val, index) => {
  console.log(`${index} ${val}`);
});
