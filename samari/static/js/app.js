$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    items: 1,
    loop: true,
    center: true,
    dots: true,
    autoplay: true
  });

  $('a[href*="#"]').on('click', function(event) {
    event.preventDefault();

    $('html, body').animate(
      { scrollTop: $($(this).attr('href')).offset().top },
      500,
      'linear'
    );
  });
});

$(window).on('load', function () {
  AOS.refresh();
});
