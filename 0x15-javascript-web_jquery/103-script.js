$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
$(document).ready(() => {
  $('#language_code').keypress(event => {
    if (event.which === 13){
      const lang = $('INPUT#language_code').val();
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
})