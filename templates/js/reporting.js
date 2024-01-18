$(document).ready(function() {
    $('.toggle').click(function() {
        $(this).siblings('ul').toggleClass('collapsed');
    });
});