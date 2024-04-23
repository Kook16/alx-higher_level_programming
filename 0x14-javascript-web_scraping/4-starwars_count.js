#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  data.results.forEach(item => {
    item.characters.forEach(val => {
      if (val === 'https://swapi-api.alx-tools.com/api/people/18/') { count++; }
    });
  });
  console.log(count);
});
