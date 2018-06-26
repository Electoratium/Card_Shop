document.addEventListener("DOMContentLoaded", getAdaptive);
window.addEventListener('resize', getAdaptive);

function  getAdaptive() {
    const deviceWidth = document.documentElement.clientWidth,
        minWidth = 1024;
    let carouselSlides = document.getElementsByClassName('carousel-inner')[0].children,
        authorImg = document.getElementsByClassName('author-img')[0].firstElementChild,
        newArrivalsItems = document.getElementsByClassName('new-item');




    function changeImagePath(elem) {
        let curPath = elem.getAttribute('src'),
            newpath = curPath.replace('small', 'large');



        elem.setAttribute('src', newpath);
    }
    if( deviceWidth >= minWidth) {
        for(let slide of carouselSlides) {
            changeImagePath(slide.children[0])
        }


        changeImagePath(authorImg);

        for(let newItem of newArrivalsItems) {
            changeImagePath(newItem.firstElementChild);
        }




    }


}