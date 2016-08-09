$(document).ready(function(){
    $("#sort-select").selectmenu();
    $("#sort-select-button").addClass("double-border");
    $(".b-addon-click").on("click", function(){
        var url_name = $(this).attr('id');
            $.ajax({
                url: "/ajax.html?name=" + url_name,
                type: "GET",
                cache: "false",
                dataType: "text",
                })
                .done(function(text){
                    $("#a-popup-title").html(text);
                })
                .fail(function( xhr, status, errorThrown ) {
                alert( "Sorry, there was a problem!" );
                console.log( "Error: " + errorThrown );
                console.log( "Status: " + status );
                console.dir( xhr );
            });

    });



})
