$(document).ready(function() {

    $('legend').click(function(){
        $(this).parent().find('.expandable_content').slideToggle("slow");
    });

});