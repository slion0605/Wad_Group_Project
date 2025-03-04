const monthYearElement = document.getElementById("monthYear");
const datesElement = document.getElementById("dates");
const prevButton = document.getElementById("prevButton");
const nextButton = document.getElementById("nextButton");


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
        datesHtml += `<div class="date ${activeClass}">${i}</div>`;
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
    
    $(document).on("click", ".date", function () {
        $(".date").removeClass("selected");
        $(this).addClass("selected");
        const selectDate = parseInt($(this).text());
        currentDate.setDate(selectDate);
        
    });
});
