const request = require("request");
const process = require("process");

filmNumber = process.argv[2];
filmEp = "https://swapi-api.alx-tools.com/api/films/" + filmNumber;
searchMovie(filmEp);

function findName(url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const person_obj = JSON.parse(body);
      console.log(person_obj.name);
    }
  });
}

function searchMovie(filmEp) {
  request.get(filmEp, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    if (response.statusCode == 200) {
      data = JSON.parse(body);
      for (let url = 0; url < data.characters.length; url++) {
        findName(data.characters[url]);
      }
    }
  });
}
