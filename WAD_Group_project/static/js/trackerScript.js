window.onload = function() {
    const xValues = document.getElementById("xValues").innerText.split(",");
    xValues.pop();  

    if (xValues.length === 0){
        document.getElementById("myChart").style.display = "none";
        document.getElementById("logMessage").style.display = "block";
    }
    const yValues = document.getElementById("yValues").innerText.split(" ");

    new Chart("myChart", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [{
                fill: false,
                lineTension: 0,
                backgroundColor: "rgba(70, 144, 67)",
                borderColor: "rgba(70, 144, 67)",
                data: yValues
            }]
        },
        options: {
            legend: { display: false }
        }
    });
};
