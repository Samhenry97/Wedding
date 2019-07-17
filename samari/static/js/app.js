$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    items: 1,
    loop: true,
    center: true,
    dots: true,
    autoplay: true
  });
});

$(window).on('load', function () {
  AOS.refresh();
});
