$(document).ready(() => {
  $('DIV#clear_list').on('click', () => {
    $('li').remove();
  });
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li:last-child').remove();
  });
});
