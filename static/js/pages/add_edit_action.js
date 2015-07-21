$(document).ready(function () {
    
    $( ".days_group" ).hide();
    $('#added_actions').hide()

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


    $('input[name="is_periodically"]').click(function() {
        if ( $(this).prop('checked') ) {
            $( ".days_group" ).show();
        }
        else{
            $( ".days_group" ).hide();
        }
    });


    $('button#add_action').click(function() {
        var table = document.getElementById("added_actions");
        var notification_time = $("#id_notification_time").val();
        var group = $("#group");
        var group_ID = group.children(':selected').val();
        var group_name = group.children(':selected').text()
        var is_periodically = $('#id_is_periodically').is(':checked');
        
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0).innerHTML="<img src="+ remove_icon +" alt='Remove' title='Remove' class='remove_icon'/> </a>";
        var cell2 = row.insertCell(1).innerHTML=group_ID;
        var cell3 = row.insertCell(2).innerHTML=group_name;
        var cell4 = row.insertCell(3).innerHTML=notification_time;
        var cell5 = row.insertCell(4).innerHTML=is_periodically;

        if ( table.rows.length > 1){
            $('#added_actions').show()
        }

    });


    $('#added_actions').on('click', 'img.remove_icon', function(e){
        $(this).closest('tr').remove();
        var table = document.getElementById("added_actions");

        if ( table.rows.length == 1){
            $('#added_actions').hide()
        }
    })

    


});