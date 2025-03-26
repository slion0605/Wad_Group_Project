$(document).ready(function(){
    console.log("catalogue.js loaded");

    $("#catalogue-accordion").accordion({
        collapsible: true,
        active: false,
        event:"mouseover",        // All panels start collapsed
        heightStyle: "content" // Accordion panels adjust to fit their content
    });
    console.log("Accordion initialized");
});