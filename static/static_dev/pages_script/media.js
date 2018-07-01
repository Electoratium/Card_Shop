document.addEventListener("DOMContentLoaded", getAdaptive);
window.addEventListener('resize', getAdaptive);

function  getAdaptive() {
    const deviceWidth = document.documentElement.clientWidth,
        deviceHeight = document.documentElement.clientHeight,
        minWidth = 1024;
    let carouselSlides = document.getElementsByClassName('carousel-inner')[0].children,
        authorImg = document.getElementsByClassName('author-img')[0].firstElementChild,
        newArrivalsItems = document.getElementsByClassName('new-item');




    function changeImagePath(elem) {

        let curPath = elem.getAttribute('src'),
            newpath = elem.getAttribute('data-largeImgUrl');



        elem.setAttribute('src', newpath);
        elem.setAttribute('data-largeImgUrl', curPath);
    }

    // ladscape  orientation smartphone
    if ( deviceWidth > deviceHeight) {

        if( deviceWidth >= minWidth) {
            for(let slide of carouselSlides) {
                changeImagePath(slide.children[0]);
            }

        }

        changeImagePath(authorImg);

        for(let newItem of newArrivalsItems) {
            changeImagePath(newItem.firstElementChild);
        }
    }
}