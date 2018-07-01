let $mainContainer = $(".main");

$mainContainer.onepage_scroll({
    easing: "cubic-bezier(0.770, 0.000, 0.175, 1.000)",                  // Easing options accepts the CSS3 easing animation such "ease", "linear", "ease-in",
    animationTime: 700,             // AnimationTime let you define how long each section takes to animate
    pagination: true,                // You can either show or hide the pagination. Toggle true for show, false for hide.
    updateURL: false,                // Toggle this true if you want the URL to be updated automatically when the user scroll to each page.
    loop: false,                     // You can have the page loop back to the top/bottom when the user navigates at up/down on the first/last page.
    keyboard: true,                  // You can activate the keyboard controls
    responsiveFallback: false,        // You can fallback to normal page scroll by defining the width of the browser in which
    direction: "vertical"            // You can now define the direction of the One Page Scroll animation. Options available are "vertical" and "horizontal". The default value is "vertical".
});

$(".arrow-container").click( () => $mainContainer.moveDown() );


$(".nav-link").click( (e) => {
 let curSlide = e.currentTarget.getAttribute('href');

 $mainContainer.moveTo(curSlide[2]);
 return false;
} );

$('.items-slider').slick({
    infinite: true,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 4,
    responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: false
          }
        },
        {
          breakpoint: 641,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
    ]
});

