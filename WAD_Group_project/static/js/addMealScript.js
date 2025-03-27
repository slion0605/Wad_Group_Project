$(document).ready(function(){
    $("h1").hide();
    $("#meal_form").hide();
    $("input[type='submit']").css("opacity", 0);


    $("h1").fadeIn(1000);
    $("#meal_form").delay(500).slideDown(1000);
    $("input[type='submit']").delay(1500).animate({opacity: 1}, 500);

    $("input[type='submit']").hover(
        function(){
            $(this).animate({backgroundColor: "#218838"}, 300);
        },
        function(){
            $(this).animate({backgroundColor: "#28a745"}, 300);
        }
    );
})