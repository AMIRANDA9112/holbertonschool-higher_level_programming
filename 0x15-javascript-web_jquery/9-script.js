// Request from API and
// displays hello value of HTML’s tag DIV#hello
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});
