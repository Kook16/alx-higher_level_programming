#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  data.results.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes(`/people/${characterId}/`)) {
        count++;
      }
    });
  });
  console.log(count);
});
