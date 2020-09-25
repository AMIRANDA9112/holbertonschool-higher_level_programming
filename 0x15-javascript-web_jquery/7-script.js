// replace name on a URL:
const url_api = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url_api, function (data, textStatus) {
  $('DIV#character').text(data.name);
});
