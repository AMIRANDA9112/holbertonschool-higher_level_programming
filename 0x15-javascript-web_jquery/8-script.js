// request all titles movies from a api
// https://swapi-api.hbtn.io/api/films/?format=json
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (response) {
    for (let i = 0; i < response.results.length; i++) {
    const movieTitle = `<li>${response.results[i].title}</li>`;
    $('ul#list_movies').append(movieTitle);
  }
});
