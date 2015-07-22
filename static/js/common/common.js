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


// Datetimepiceker settings
    $('.form_datetime').datetimepicker({
        //language:  'fr',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        forceParse: 0,
        showMeridian: 1
    });
    $('.form_date').datetimepicker({
        language:  'fr',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0
    });
    $('.form_time').datetimepicker({
        language:  'fr',
        weekStart: 1,
        todayBtn:  1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 1,
        minView: 0,
        maxView: 1,
        forceParse: 0
    });



});