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

