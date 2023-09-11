#!/usr/bin/node

// script that prints the first argument passed to it:

let message;

if (process.argv[2])
    message = process.argv[2];
else
    message = 'No argument';

console.log(message);
