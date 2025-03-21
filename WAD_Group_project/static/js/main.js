// calender stuff 
// templated used from https://www.youtube.com/watch?v=OcncrLyddAs

const monthYearElement = document.getElementById("monthYear");
const datesElement = document.getElementById("dates");
const prevButton = document.getElementById("prevButton");
const nextButton = document.getElementById("nextButton");
const logDates = JSON.parse(document.getElementById('logDates').textContent);
console.log(logDates);

let currentDate = new Date();


const updateCalendar = () => {
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();

    const firstDay = new Date(currentYear, currentMonth, 0);
    const lastDay = new Date(currentYear, currentMonth + 1, 0);
    const totalDays = lastDay.getDate();
    const firstDayIndex = firstDay.getDay();
    const lastDayIndex = lastDay.getDay();

    const monthYearString = currentDate.toLocaleString('default', { month: 'long', year: 'numeric' });
    monthYearElement.textContent = monthYearString;

    let datesHtml = '';

    
    for (let i = firstDayIndex; i > 0; i--) {
        const prevDate = new Date(currentYear, currentMonth, 0 -i + 1);
        datesHtml += `<div class="date inactive">${prevDate.getDate()}</div>`;
    }

  
    for (let i = 1; i <= totalDays; i++) {
        const date = new Date(currentYear, currentMonth, i);
        const activeClass = date.toDateString() === new Date().toDateString() ? 'active' : '';
        datesHtml += `<div class="date ${activeClass} >${i}</div>`;
    }

  
    for (let i = 1; i <= 7 - lastDayIndex; i++) {
        const nextDate = new Date(currentYear, currentMonth + 1, i);
        datesHtml += `<div class="date inactive">${nextDate.getDate()}</div>`;
        
    }

    datesElement.innerHTML = datesHtml;
}

prevButton.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    updateCalendar();
})

nextButton.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    updateCalendar();
});


updateCalendar();



$(document).ready(function () {
    let visibleElement = null
    
    $(document).on("click", ".date", function () {
        if ($(this).hasClass("inactive")) return;
        $(".date").removeClass("selected");
        $(this).addClass("selected");
        
        let selectedDate = parseInt($(this).text());
        currentDate.setDate(selectedDate);
        
        let formattedDate = `${selectedDate} ${monthYearElement.textContent}`;
        
        if(visibleElement != null ){
            document.getElementById(visibleElement).style.display = "none";
        }
        document.getElementById(formattedDate).style.display = "block";
       
        visibleElement = formattedDate;
    });

    $("#addMeal").on("click", function() {
        location.href = '/fitnessTracker/add_meal/'; 
    });

    $("#addWorkout").on("click", function() {
        location.href = '/fitnessTracker/add_workout/'; 
    });

    $("#addLog").on("click", function() {
        location.href = '/fitnessTracker/add_log/'; 
    });

});
