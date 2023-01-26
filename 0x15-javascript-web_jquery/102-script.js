$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
