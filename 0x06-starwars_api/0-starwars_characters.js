#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));
const filmId = process.argv[2];

// Function to fetch Star Wars characters based on film ID
async function fetchStarWarsCharacters(filmId) {
  try {
    // Construct API endpoint for fetching film details
    const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    let filmResponse = await request(filmUrl);
    let filmData = JSON.parse(filmResponse.body);
    
    // Extract characters' URLs from the film data
    const characterUrls = filmData.characters;

    // Iterate through each character URL and fetch their name
    for (const url of characterUrls) {
      let characterResponse = await request(url);
      let characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Call the function with the provided film ID
fetchStarWarsCharacters(filmId);
