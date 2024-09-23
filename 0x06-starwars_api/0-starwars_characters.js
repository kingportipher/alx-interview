#!/usr/bin/node
/**
 * Script to fetch and display Star Wars movie characters.
 */

const request = require('request');

// Check if a Movie ID was passed as a command-line argument
if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch the movie details based on the Movie ID
request(apiUrl, (err, response, body) => {
  if (err || response.statusCode !== 200) {
    console.error('Error fetching data:', err || `Status Code: ${response.statusCode}`);
    return;
  }

  // Parse the response and retrieve the list of character URLs
  const characters = JSON.parse(body).characters;
  
  // Fetch and display each character's name
  getCharacterNames(characters);
});

// Function to fetch and print character names recursively
function getCharacterNames(characterUrls, index = 0) {
  if (index === characterUrls.length) return; // Stop when all characters are processed

  request(characterUrls[index], (err, response, body) => {
    if (!err && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      getCharacterNames(characterUrls, index + 1); // Process next character
    } else {
      console.error('Error fetching character:', err || `Status Code: ${response.statusCode}`);
    }
  });
}
