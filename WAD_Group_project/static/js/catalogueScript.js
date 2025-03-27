
$(document).ready(function () {
    $("[id^='browse-']").click(function () {
        let key = $(this).attr("id").replace("browse-", "");
        document.getElementById(key + "-info").style.display = "block"; 
    });
});