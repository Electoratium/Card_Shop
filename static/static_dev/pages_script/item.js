
$('#slider').slick({
     slidesToShow: 1,
     slidesToScroll: 1,
     arrows: false,
     fade: true,
     asNavFor: '#slider-nav'
});



const nmbSlides = document.getElementById('slider-nav').childElementCount,
    maxSlides = 4,
    maxNmbSlides = nmbSlides > 5 ? maxSlides :  nmbSlides === 1 ? 1 : nmbSlides - 1,
    mediumNmbSlides = maxNmbSlides > 1 ? maxNmbSlides - 1 : 1,
    smallNmbSlides = mediumNmbSlides > 1 ? mediumNmbSlides - 1 : 1,
    xsSmallNmbSlides = smallNmbSlides > 1 ? smallNmbSlides - 1 : 1;


$('#slider-nav').slick({
    slidesToShow: maxNmbSlides,
    slidesToScroll: maxNmbSlides,
    asNavFor: '#slider',
    infinite: true,
    dots: false,
    focusOnSelect: true,
    responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: mediumNmbSlides,
            slidesToScroll: mediumNmbSlides,
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


const form = document.getElementById('orderForm');



form.addEventListener('submit', hideForm);

function hideForm(e) {
    e.preventDefault();

    const method = form.getAttribute('method'),
        url = form.getAttribute('action');

    let data = {};

    for(let field of form.elements) {
       let fieldName = field.getAttribute('name');

       data[fieldName] = field.value;
    }

    form.classList.add('hidden');

    $.ajax({
        data: data,
        type: method,
        url: url,
        success: function(response) {
            showResponseBanner('success');
        },
        error: function(e, x, r) {
            showResponseBanner('error');
        }
    });


    function showResponseBanner(result) {
        let banner = document.getElementById('sendingResult'),
            titleBanner = banner.firstElementChild,
            textBanner = banner.lastElementChild;


        if(result === 'success') {
            banner.classList.add('alert-success');
            titleBanner.innerHTML = 'Спасибо!';
            textBanner.innerHTML = 'С вами свяжуться в ближайшее время.';
        }
        else if (result === 'error') {
            banner.classList.add('alert-danger');
            titleBanner.innerHTML = 'Ошибка';
            textBanner.innerHTML = 'Возникла ошибка на сервере при отправке ваших данных, перезагрузите страничку и попробуйте ещё раз.';
        }
        banner.classList.remove('hidden');
    }
}


$('#accordion').on('shown.bs.collapse', scrollDown);

function scrollDown() {
    const deviceHeight = window.innerHeight,
        fullHeightContent = document.body.clientHeight,
        scrollHeight = fullHeightContent - deviceHeight;

    if (scrollHeight) window.scrollBy(0, scrollHeight);
}

