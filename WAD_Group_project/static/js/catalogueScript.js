$(document).ready(function(){
    console.log("catalogue.js loaded");

    $("#catalogue-accordion").accordion({
        collapsible: true,
        active: false,
        event:"mouseover",       
        heightStyle: "content" 
    });
    console.log("Accordion initialized");
});