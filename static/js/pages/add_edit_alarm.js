$(document).ready(function () {
    
    $('#monday, #tuesday, #thursday, #friday, #saturday, #wednesday, #sunday').click(function(){
        if ( $(this).hasClass('btn btn-xs btn-default')){
            $( this ).removeClass("btn btn-xs btn-default");
            $( this ).addClass("btn btn-xs btn-success");
        }
        else{
            $( this ).removeClass("btn btn-xs btn-success");
            $( this ).addClass("btn btn-xs btn-default");   
        }
    });

});