$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
  if ($('header').hasClass('red') && $('header').hasClass('green')) {
    if ($('header').hasClass('red')) {
      $('header').removeClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('red');
    }
  }
});
