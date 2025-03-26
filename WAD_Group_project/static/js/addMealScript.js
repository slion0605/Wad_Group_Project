$(document).ready(function () {
    const $heading = $("h1");
    const $form = $("#meal_form");
    const $submit = $("input[type='submit']");

   
    $heading.hide();
    $form.hide();
    $submit.css("opacity", 0);

   
    $heading.fadeIn(1000);
    $form.delay(500).slideDown(1000);
    $submit.delay(1500).animate({ opacity: 1 }, 500);


    $submit.hover(
        function () {
            $(this).stop().animate({ backgroundColor: "#218838" }, 300);
        },
        function () {
            $(this).stop().animate({ backgroundColor: "#28a745" }, 300);
        }
    );
});