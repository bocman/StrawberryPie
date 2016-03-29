/*

Here is the javascript code, which is common used all over the application
 
 */


$(document).ready(function() {


    //Fieldsets settings to show/hide content
    $('legend').click(function(){
        var icon = $(this).find('.icon');
        var content = $(this).parent().find('.fieldset_content');
        
        content.slideToggle("slow");
        if( icon.attr('src') == paths["fieldset_close"] ){ 
            icon.attr("src", paths["fieldset_open"]);
        }
        else{
           icon.attr("src", paths["fieldset_close"]); 
        }
    });



});