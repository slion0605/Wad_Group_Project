window.onload = function() {
    const xValues = document.getElementById("xValues").innerText.split(",");
    xValues.pop();  

    if (xValues.length === 0){
        document.getElementById("myChart").style.display = "none";
        document.getElementById("logMessage").style.display = "block";
    }
    const caloriesValues = document.getElementById("caloriesValue").innerText.split(",").map(Number);;
    const proteinValues = document.getElementById("proteinValue").innerText.split(",").map(Number);;
    const carbsValues = document.getElementById("carbsValue").innerText.split(",").map(Number);;
    const fatValues = document.getElementById("fatValue").innerText.split(",").map(Number);;

    new Chart("myChart", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [
                {
                    label: "Calories",
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(68, 179, 66, 0.46)",
                    borderColor: "rgb(73, 171, 34)",
                    data: caloriesValues
                },
                {
                    label: "Protein",
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(54, 162, 235, 0.5)",
                    borderColor: "rgba(54, 162, 235, 1)",
                    data: proteinValues
                },
                {
                    label: "Carbs",
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(145, 118, 48, 0.5)",
                    borderColor: "rgb(185, 150, 61)",
                    data: carbsValues
                },
                {
                    label: "Fat",
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(55, 53, 203, 0.64)",
                    borderColor: "rgb(73, 63, 211)",
                    data: fatValues
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: { display: true },
            scales: {
                y: {
                    type: "logarithmic",
                    beginAtZero: true,
                    ticks: {
                        stepSize: 100
                    }

                }
            }
        }
    });
};
