$(document).ready(function () {
    $('.nav-toggle').on('click', function () {
        // Toggle the menu visibility
        $('.menu').toggleClass('menu-open');
    });

    // Close menu when clicking outside of it
    $(document).on('click', function (event) {
        if (!$(event.target).closest('.primary-nav').length) {
            $('.menu').removeClass('menu-open');
        }
    });

    // Close menu when the cursor leaves the menu
    $('.menu').mouseleave(function () {
        $('.menu').removeClass('menu-open');
    });
});


