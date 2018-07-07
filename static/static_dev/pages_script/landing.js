$('document').ready(function () {

    let $mainContainer = $(".main");

    $mainContainer.onepage_scroll({
        easing: "cubic-bezier(0.770, 0.000, 0.175, 1.000)",
        animationTime: 700,
        pagination: true,
        updateURL: false,
        loop: false,
        keyboard: true,
        responsiveFallback: false,
        direction: "vertical"
    });

    $(".arrow-container").click( () => $mainContainer.moveDown() );


    $(".grid-nav").click( (e) => {
        try {
            let curSlide = e.target.getAttribute('href');
            $mainContainer.moveTo(curSlide[2]);
        }
        catch (TypeError) {
        }
     return false;
    } );



    const nmbSlides = document.getElementsByClassName('items-slider')[0].childElementCount,
        maxSlides = 4,
        maxNmbSlides = nmbSlides > 5 ? maxSlides :  nmbSlides === 1 ? 1 : nmbSlides - 1,
        mediumNmbSlides = maxNmbSlides > 1 ? maxNmbSlides - 1 : 1,
        smallNmbSlides = mediumNmbSlides > 1 ? mediumNmbSlides - 1 : 1,
        xsSmallNmbSlides = smallNmbSlides > 1 ? smallNmbSlides - 1 : 1;


    $('.items-slider').slick({
    infinite: true,
    speed: 300,
    slidesToShow: maxNmbSlides,
    slidesToScroll: maxNmbSlides,
    responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: mediumNmbSlides,
            slidesToScroll: mediumNmbSlides,
            infinite: true,
            dots: false
          }
        },
        {
          breakpoint: 641,
          settings: {

            slidesToShow: smallNmbSlides,
            slidesToScroll: smallNmbSlides
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: xsSmallNmbSlides,
            slidesToScroll: xsSmallNmbSlides
          }
        }
    ]
    });
});