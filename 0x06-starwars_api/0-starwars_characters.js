#!/usr/bin/node

const request = require('request');

function fetchCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  });
}

const movieId = process.argv[2];
fetchCharacters(movieId);
