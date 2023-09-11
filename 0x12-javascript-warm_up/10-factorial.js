#!/usr/bin/node

// a script that computes and prints a factorial

function fact (num) {
  if (isNaN(num) || num === 1 || num === 0) { return 1; }

  return num * fact(num - 1);
}

const num = parseInt(process.argv[2]);

console.log(fact(num));
