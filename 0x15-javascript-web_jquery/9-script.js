const settings = {
  cache: false,
  dataType: 'json',
  async: true,
  crossDomain: true,
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  method: 'GET',
  headers: {
    accept: 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*'
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
