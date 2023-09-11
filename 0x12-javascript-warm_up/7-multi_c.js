#!/usr/bin/node

// script that prints x times “C is fun”


const times = process.argv[2];

if (!times)
    console.log('Missing number of occurrences');
else if (times !== NaN && times >= 0) {
    let i = 0;
    while (i < times)
    {
	console.log('C is fin');
	i++;
    }
}
