$('.env').hide();
$('.spe').click(function() {
  $('.env').fadeIn();
});

$('.add button').click(function() {
  var matiereVal = $('#matiere').val(),
    jourVal = $('#jour').val(),
    debutVal = $('#debut').val(),
    debutVal = parseInt(debutVal),
    dureeVal = $('#duree').val(),
    dureeVal = parseInt(dureeVal),
    couleurVal = $('#color').val();
  limit = debutVal + dureeVal;
  for (debutVal; debutVal < limit; debutVal++) {

    $("td[data-h=" + debutVal + "][data-j=" + jourVal + "]").css({
      'background-color': couleurVal,
      'border-bottom': 'none'
    }).empty().append(matiereVal);
  }
  $('.env').fadeOut();
});

$('td').click(function() {
  if ($(this).attr('class') == "f") {

  } else {
    $(this).toggleClass('active').attr('style', '');

    $('.leftContent').fadeIn();
    $('.leftContent .addButton').click(function() {
      val = $('#pop').val(),
        colorVal = $('.leftContent input[type=color]').val();
      $('.active').css({
        'background-color': colorVal,
        'border-bottom': 'none'
      }).empty().append(val).removeClass();
    });
  }
});
$('.leftContent .red').click(function() {
  $('.active').empty().removeClass().css({
    'background-color': 'initial',
    'border-bottom': '1px solid lightgrey'
  });
});
$('td').dblclick(function() {
  $('td').removeClass('active');
});