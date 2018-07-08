document.addEventListener('DOMContentLoaded', getAdaptive);
window.addEventListener('resize', getAdaptive);

let defaultOrientationImg = 'portrait';
function getAdaptive() {
    const deviceWidth = document.documentElement.clientWidth,
        deviceHeight = document.documentElement.clientHeight,
        curOrientation = deviceWidth > deviceHeight ? 'landscape': 'portrait',
        slidesImages = document.getElementsByClassName('item-image');



    function changeOrientationImg(elem) {
        if(elem) {
            let curPath = elem.getAttribute('src'),
                newpath = elem.getAttribute('data-new-orientation-img');


            elem.setAttribute('src', newpath);
            elem.setAttribute('data-new-orientation-img', curPath);
        }

    }


    if (defaultOrientationImg !== curOrientation) {
        for (let sliderImage of slidesImages) {

            changeOrientationImg(sliderImage.children[0]);
        }


        defaultOrientationImg = curOrientation;
    }
}