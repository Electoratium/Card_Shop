 $('#slider').slick({
     slidesToShow: 1,
     slidesToScroll: 1,
     arrows: false,
     fade: true,
     asNavFor: '#slider-nav'
});
$('#slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '#slider',
    dots: false,
    centerMode: true,
    focusOnSelect: true
});


let form = document.getElementById('orderForm');

form.addEventListener('submit', hideForm);

function hideForm(e) {
    e.preventDefault();

    form.classList.add('hidden');

    document.getElementById('success').classList.remove('hidden');
}


$('#accordion').on('shown.bs.collapse', scrollDown);

function scrollDown() {
    const deviceHeight = window.innerHeight,
        fullHeightContent = document.body.clientHeight,
        scrollHeight = fullHeightContent - deviceHeight;

    if (scrollHeight) window.scrollBy(0, scrollHeight);
}

