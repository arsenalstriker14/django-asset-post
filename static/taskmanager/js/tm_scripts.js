$(document).ready(function() {
    $( "#list_in" ).click(function() {
        $('.tlist').css('display', 'none');
        $('#personal_tlist').fadeIn(1000, function() { });
    });
    $( "#list_out" ).click(function() {
        $('.tlist').css('display', 'none');
        $('#assigned_tlist').fadeIn(1000, function() { });
    }); 
    $( "#list_studio" ).click(function() {
        $('.tlist').css('display', 'none');
        $('#studio_tlist').fadeIn(1000, function() { });
    });
    $( "#list_creative" ).click(function() {
        $('.tlist').css('display', 'none');
        $('#creative_tlist').fadeIn(1000, function() { });
    });                 
});

