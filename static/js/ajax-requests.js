"use strict";

//READY STATES(JQuery takes care of this for us. Just found it interesting :):

// 0 request not initialized
// 1 request has been set up
// 2 request has been sent
// 3 request is in process
// 4 request is complete


// Future AJAX queries may go here. 


// use this function to update your html div
function updateTrip(results) {

    console.log(results)
    $('trip-details').html("<p>" + results.campsite_name + "</p>");
}

function addTrip(evt) {
    evt.preventDefault();

    let formInputs = {
        "campsite_name": $marker.properties.title.val()
    };

    console.log("addTrip formInputs:")
    console.log(formInputs)

    $.post("/trip_details.json", formInputs, updateTrip);
}


$("#add_to_trip").on('click', addTrip);





