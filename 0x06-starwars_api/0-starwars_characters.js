#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.log('Please provide a movie ID');
  process.exit(1);
}

// SWAPI Films endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the request to get movie data
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movieData = JSON.parse(body);

  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

