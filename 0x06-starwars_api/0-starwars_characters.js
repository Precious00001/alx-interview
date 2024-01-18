#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Extract the film number from the command line arguments
const filmNum = process.argv[2] + '/';

// Define the URL for the Star Wars API (SWAPI) films
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film information
request(filmURL + filmNum, async function(err, res, body) {
  // Check for errors in the request
  if (err) return console.error(err);

  // Parse the response body to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Iterate through the character URLs and fetch character information
  // Make a request to each character URL
  for (const charURL of charURLList) {
    // Use a Promise to handle the asynchronous nature of requests
    await new Promise(function(resolve, reject) {
      // Make a request to the individual character URL
      request(charURL, function(err, res, body) {
        // Check for errors in the request
        if (err) return console.error(err);

        // Parse the character information and print the character's name
        console.log(JSON.parse(body).name);

        // Resolve the promise to indicate completion
        resolve();
      });
    });
  }
});