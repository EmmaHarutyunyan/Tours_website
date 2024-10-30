
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('myModal');
    const btn = document.getElementById('myBtn');
    const span = document.getElementsByClassName('close')[0];

    btn.onclick = function() {
        modal.style.display = 'block';
    }

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
});

document.addEventListener('DOMContentLoaded', function () {
    function updateLanguage(input) {
        input.form.submit();
    }

    const languageOptions = document.querySelectorAll('.language-option input[type="radio"]');

    languageOptions.forEach(option => {
        option.addEventListener('change', function () {
            const selectedLanguage = this.value;
            console.log('Selected language:', selectedLanguage);
        });
    });
});

function changeLanguage(value) {
    var form = document.getElementById('language-form');
    var input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'language';
    input.value = value;
    form.appendChild(input);
    form.submit();
}

document.addEventListener('DOMContentLoaded', () => {
    const sideGallery = document.querySelector('.side-gallery');
    const sideGalleryItems = document.querySelectorAll('.side-gallery-item');
    const visibleItemsCount = 3;
    const itemHeight = sideGalleryItems[0].offsetHeight;
    const totalHeight = itemHeight * sideGalleryItems.length;

    const cloneGallery = sideGallery.cloneNode(true);
    sideGallery.appendChild(cloneGallery);

    sideGallery.style.transform = `translateY(0px)`;

    function startSlider() {
        let currentOffset = 0;

        function slide() {
            currentOffset += itemHeight;
            if (currentOffset >= totalHeight) {
                currentOffset = 0;
                sideGallery.style.transition = 'none';
                sideGallery.style.transform = `translateY(${currentOffset}px)`;
                setTimeout(() => {
                    sideGallery.style.transition = 'transform 1s ease-in-out';
                    sideGallery.style.transform = `translateY(-${itemHeight * visibleItemsCount}px)`;
                }, 50);
            } else {
                sideGallery.style.transform = `translateY(-${currentOffset}px)`;
            }
        }

        sideGallery.style.transition = 'transform 1s ease-in-out';
        sideGallery.style.transform = `translateY(-${itemHeight * visibleItemsCount}px)`;
        setInterval(slide, 3000);
    }

    startSlider();
});

document.addEventListener('DOMContentLoaded', () => {
    const scrollUpBtn = document.querySelector('.scroll-up');
    const scrollDownBtn = document.querySelector('.scroll-down');
    const toursContainer = document.querySelector('.tours-container');

    let scrollAmount = 100;
    let scrollInterval = 10;
    let accelerationRate = 5;
    let maxScrollAmount = 1000;

    let scrollIntervalId;
    let scrollTimeoutId;

    function startScrolling(direction) {
        function accelerateScroll() {
            if (scrollAmount < maxScrollAmount) {
                scrollAmount *= accelerationRate;
                if (scrollAmount > maxScrollAmount) {
                    scrollAmount = maxScrollAmount;
                }
            }
            toursContainer.scrollBy({
                top: direction === 'up' ? -scrollAmount : scrollAmount,
                behavior: 'smooth'
            });
            scrollTimeoutId = setTimeout(accelerateScroll, scrollInterval);
        }

        accelerateScroll();

        scrollIntervalId = setInterval(() => {
            toursContainer.scrollBy({
                top: direction === 'up' ? -scrollAmount : scrollAmount,
                behavior: 'smooth'
            });
        }, scrollInterval);
    }

    function stopScrolling() {
        clearInterval(scrollIntervalId);
        clearTimeout(scrollTimeoutId);
        scrollAmount = 100;
    }

    scrollUpBtn.addEventListener('mousedown', () => startScrolling('up'));
    scrollDownBtn.addEventListener('mousedown', () => startScrolling('down'));

    scrollUpBtn.addEventListener('mouseup', stopScrolling);
    scrollDownBtn.addEventListener('mouseup', stopScrolling);

    scrollUpBtn.addEventListener('mouseleave', stopScrolling);
    scrollDownBtn.addEventListener('mouseleave', stopScrolling);

    function handleMouseWheel(event) {
        event.preventDefault();
        const delta = event.deltaY;

        const wheelScrollAmount = Math.min(Math.abs(delta) * 2, maxScrollAmount);
        toursContainer.scrollBy({
            top: delta > 0 ? wheelScrollAmount : -wheelScrollAmount,
            behavior: 'smooth'
        });
    }

    toursContainer.addEventListener('wheel', handleMouseWheel);
});

document.addEventListener("DOMContentLoaded", function () {
    const videos = document.querySelectorAll('video');

    videos.forEach(function(video) {
        video.addEventListener('ended', function() {
            video.currentTime = 0;
            video.play();
        });

        video.play();
    });

    const bookedDates = JSON.parse('{{ booked_dates|escapejs }}');

    const disableBookedDates = (inputElement) => {
        inputElement.addEventListener('input', function () {
            const date = new Date(this.value);
            for (let i = 0; i < bookedDates.length; i++) {
                const [start_date, end_date] = bookedDates[i];
                const startDate = new Date(start_date);
                const endDate = new Date(end_date);

                if (date >= startDate && date <= endDate) {
                    this.value = '';
                    alert("{% trans 'Selected date is not available. Please choose a different date.' %}");
                }
            }
        });
    };

    const startDateInput = document.getElementById("start_date");
    const endDateInput = document.getElementById("end_date");

    disableBookedDates(startDateInput);
    disableBookedDates(endDateInput);
    
    flatpickr("#start_date", {
        dateFormat: "Y-m-d",
        disable: bookedDates.flat(),
        minDate: '{{ today }}',
    });

    flatpickr("#end_date", {
        dateFormat: "Y-m-d",
        disable: bookedDates.flat(),
        minDate: '{{ today }}',
    });

    let slideIndex = 0;

    function showSlides() {
        const slides = document.getElementsByClassName("slide");
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1 }
        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 5000);
    }

    showSlides();

    function plusSlides(n) {
        slideIndex += n;
        if (slideIndex > document.getElementsByClassName("slide").length) { slideIndex = 1 }
        if (slideIndex < 1) { slideIndex = document.getElementsByClassName("slide").length }
        showSlides();
    }

    document.querySelector(".prev").addEventListener("click", function () {
        plusSlides(-1);
    });

    document.querySelector(".next").addEventListener("click", function () {
        plusSlides(1);
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "ArrowLeft") {
            plusSlides(-1);
        } else if (event.key === "ArrowRight") {
            plusSlides(1);
        }
    });
});
