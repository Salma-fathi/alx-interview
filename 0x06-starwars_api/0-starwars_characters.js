#!/usr/bin/node

const request = require('request');
const { text } = require('stream/consumers');
const util = require('util');

// Convert request to promise-based
const requestAsync = util.promisify(request);

// Base URL for Star Wars API
const BASE_URL = 'https://swapi.dev/api';

async function getCharactersFromMovie(movieId) {
  try {
    // Get movie data
    const movieResponse = await requestAsync(`${BASE_URL}/films/${movieId}/`);
    const movieData = JSON.parse(movieResponse.body);
    const characterUrls = movieData.characters;

    // Get all characters
    const characterPromises = characterUrls.map(url => requestAsync(url));
    const characterResponses = await Promise.all(characterPromises);

    // Extract and print character names in order
    characterResponses.forEach(response => {
      const character = JSON.parse(response.body);
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Get movie ID from command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

// Execute the main function
getCharactersFromMovie(movieId);
