const request = require("request");

function getCharacterNames(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error("Error:", error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error("Error:", response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Function to recursively print character names
    function printCharacters(index) {
      if (index === characterUrls.length) {
        return;
      }

      request(characterUrls[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error("Error:", charError);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }

        printCharacters(index + 1);
      });
    }

    // Start printing character names
    printCharacters(0);
  });
}
