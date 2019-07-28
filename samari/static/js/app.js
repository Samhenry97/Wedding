let sticky = null;

$(document).ready(function() {
  // Owl Carousel for Quotes
  $('.owl-carousel').owlCarousel({
    items: 1,
    loop: true,
    center: true,
    dots: true,
    autoplay: true
  });

  // Smooth Scroll
  $('a[href*="#"]').on('click', function(event) {
    event.preventDefault();

    $('html, body').animate(
      { scrollTop: $($(this).attr('href')).offset().top },
      1500,
      'easeInOutQuint'
    );
  });

  // Ensure on-scroll animations are correct
  AOS.refresh();

  // Mobile Menu
  $('#hamburger').click(function(event) {
    $('#nav-items-mobile').addClass('slide-in');
  });
  $('#nav-items-mobile').click(function(event) {
    $('#nav-items-mobile').removeClass('slide-in');
  });

  // Custom viewport pixels to support mobile
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);

  // Calculate the header's sticky position
  sticky = $('#home')[0].getBoundingClientRect().bottom + window.scrollY;
});

window.addEventListener('resize', function() {
  sticky = $('#home')[0].getBoundingClientRect().bottom + window.scrollY;
});

// Determind if sticky header should stick
window.addEventListener('scroll', function() {
  if(window.scrollY > sticky) {
    $('header').addClass('sticky');
  } else {
    $('header').removeClass('sticky');
  }
});
