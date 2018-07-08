document.addEventListener('DOMContentLoaded', getAdaptive);
window.addEventListener('resize', getAdaptive);


let defaultOrientationImg = 'portrait';

function  getAdaptive() {
    const deviceWidth = document.documentElement.clientWidth,
        deviceHeight = document.documentElement.clientHeight,
        resizeTextDeviceWidth = 568,
        maxLenText = 200;
    let carouselSlides = document.getElementsByClassName('carousel-inner')[0].children,
        authorImg = document.getElementsByClassName('author-img')[0].firstElementChild,
        authorDescription = document.getElementsByClassName('author-descr')[0].firstElementChild,
        newArrivalsItems = document.getElementsByClassName('new-item'),
        curOrientation = deviceWidth > deviceHeight ? 'landscape': 'portrait';



    function changeImagePath(elem) {

        let curPath = elem.getAttribute('src'),
            newpath = elem.getAttribute('data-largeImgUrl');


        elem.setAttribute('src', newpath);
        elem.setAttribute('data-largeImgUrl', curPath);
    }

    function resizeText() {
        let curDescr = authorDescription.innerHTML;

        if (curDescr.length >= maxLenText) {
            authorDescription.innerHTML = `${curDescr.substring(0, maxLenText)}...`;
        }
    }

   function changeOrientationImage() {
        for(let slide of carouselSlides) {
            changeImagePath(slide.children[0]);
        }

        changeImagePath(authorImg);

        for(let newItem of newArrivalsItems) {
            changeImagePath(newItem.firstElementChild);
        }
   }


    if (defaultOrientationImg !== curOrientation) {
        changeOrientationImage();


        defaultOrientationImg = curOrientation;
    }

    if (deviceWidth <= resizeTextDeviceWidth) {
        resizeText();
    }
}