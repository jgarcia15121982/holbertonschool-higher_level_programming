$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      const results = data.results;
      for (const result of results) {
        $('UL#list_movies').append('<li>' + result.title + '</li>');
      }
    }
  });
});
