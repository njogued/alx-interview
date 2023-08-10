#!/usr/bin/node

const request = require("request");

const episode = process.argv[2];
const episodeEndpoint = "https://swapi-api.alx-tools.com/api/films" + episode;

function sendRequest(characterList, index) {
  // Base case: stop when index reaches the length of characterList
  if (characterList.length === index) {
    return;
  }
  // Make a request for the character at the current index
  request(characterList[index], (error, response, body) => {
    if (error) {
      // Log error if there's an issue with the request
      console.log(error);
    } else {
      // Log the name of the character from the response body
      console.log(JSON.parse(body).name);
      // Recursively call sendRequest for the next character
      sendRequest(characterList, index + 1);
    }
  });
}

request(episodeEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;
    sendRequest(characterList, 0);
  }
});
