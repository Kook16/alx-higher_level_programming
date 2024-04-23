#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // Get movie ID from command-line argument

if (!movieId) {
    console.error('Usage: ./100-starwars_characters.js <MOVIE_ID>');
    process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error.message);
        return;
    }
    if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
        return;
    }

    try {
        const data = JSON.parse(body);
        const characters = data.characters;

        // Function to fetch character names
        const getCharacterNames = async () => {
            for (const characterUrl of characters) {
                const characterResponse = await new Promise((resolve, reject) => {
                    request(characterUrl, (error, response, body) => {
                        if (error) {
                            reject(error);
                            return;
                        }
                        if (response.statusCode !== 200) {
                            reject(`Unexpected status code: ${response.statusCode}`);
                            return;
                        }
                        resolve(JSON.parse(body).name);
                    });
                });
                console.log(characterResponse);
            }
        };

        // Call function to fetch character names
        getCharacterNames();
    } catch (parseError) {
        console.error('Error parsing response body:', parseError.message);
    }
});
