document.addEventListener('DOMContentLoaded', hidePreloader);

   document.body.classList.add('hideScrollBar');

function hidePreloader() {
    const preloader = document.getElementById('preloader');

    document.body.classList.remove('hideSrollBar');
    preloader.classList.add('d-none');
}

