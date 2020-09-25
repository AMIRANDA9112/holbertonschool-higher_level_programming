// fetches and prints how to say “Hello”
// depending on the language
const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(document).ready(function () {
  $('input#btn_translate').click(function () {
      const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (info) {
      $('div#hello').text(info.hello);
    });
  });
});
