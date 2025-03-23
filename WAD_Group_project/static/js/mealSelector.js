$(document).ready(function () {
    $("#edit").click(function () {
        $("#edit-profile-section").toggle();
    });

    $("#profile-form").on("submit", function (event) {
        event.preventDefault(); 
        
        $.ajax({
            url: "{% url 'fitnessTracker:update_profile' %}",
            method: "POST",
            data: $(this).serialize(),
            success: function (response) {
                if (response.status === "success") {
                    $("#weight").text(response.data.weight);
                    $("#experience").text(response.data.experience);
                    $("#goal").text(response.data.goal);

                    $("#edit-profile-section").hide();
                } else {
                    alert(response.message);  
                }
            },
            error: function () {
                alert("Error updating the profile. Please try again.");
            }
        });
    });

    $('#meal-select').on("change", function(){
        var mealId = $(this).val();
        if (mealId){
            $.ajax({
                url: "{% url 'fitnessTracker:get_meal' %}",
                type: "GET",
                data: {'meal_id': mealId},
                success: function(response){
                    $('#meal-name').text(response.name);
                    $('#meal-calories').text("Calories: " + response.calories);
                    $('#meal-protein').text("Protein: " + response.protein);
                    $('#meal-fat').text("Fat: " + response.fat);
                    $('#meal-carbohydrates').text("Carbohydrates: " + response.carbohydrate);
                    $('#meal-description').text("Description: " + response.description);
                    $('.meal-details').show();
                },
                error: function(){
                    alert("Error on getting meal details");
                }
            });
        } else {
            $(".meal-details").hide();
        }
    });

    $('#edit-meal-btn').click(function(){
        $('#edit-form').toggle();
    });

    $('#save-description-btn').on('click', function(){
        var meal_id = $('#meal-select').val();
        var new_description = $('#new-description').val()
        $.ajax({
            url: "{% url 'fitnessTracker:update_meal' %}",
            method: 'POST',
            data: {
                'meal_id': meal_id,
                'description': new_description,
            },
            success: function(response){
                if (response.status === "success"){
                    $('#meal-description').text(response.data);
                    $('#edit-form').hide();
                    alert("Meal description changed successfully")
                } else {
                    alert("Error: " + response.message);
                }
            },
            error: function () {
                alert("Error updating the meal. Please try again.");
            }
        });
    });
});