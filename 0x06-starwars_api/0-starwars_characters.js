#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Define the base URL for the Star Wars API
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if the command line has at least 3 arguments (including script name)
if (process.argv.length > 2) {
  // Make a GET request to retrieve information about a specific film
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }

    // Parse the film information to get URLs of characters in the film
    const charactersURL = JSON.parse(body).characters;

    // Use Promise.all to asynchronously fetch and resolve character names
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make a request to each character URL
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }

          // Parse the character information and resolve with the character's name
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // When all promises are resolved, print the character names
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
