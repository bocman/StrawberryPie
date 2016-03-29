$(document).ready(function () {

    $(function () {
        $('#datetimepicker1').datetimepicker();
    });
    $(function () {
        $('#end_time_picker').datetimepicker();
    });

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
            $( "#days_group" ).show();
        }
        else{
            $( "#days_group" ).hide();
        }
    });


    $('button#add_event').click(function() {
        var table = document.getElementById("added_events");
        var start_time = $("[name='start_time']").val();
        var end_time = $("[name='end_time']").val();
        var group = $("#group");
        var group_ID = group.children(':selected').val();
        var group_name = group.children(':selected').text()
        var is_periodically = $('#id_is_periodically').is(':checked');
        
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0).innerHTML="<img src="+ remove_icon +" alt='Remove' title='Remove' class='remove_icon'/> </a>";
        var cell2 = row.insertCell(1).innerHTML=group_ID;
        var cell3 = row.insertCell(2).innerHTML=group_name;
        var cell4 = row.insertCell(3).innerHTML=start_time;
        var cell5 = row.insertCell(4).innerHTML=end_time;
        var cell6 = row.insertCell(5).innerHTML=is_periodically;

        if ( table.rows.length > 1){
            $('#added_events').show()
        }

    });


    $('#added_events').on('click', 'img.remove_icon', function(e){
        $(this).closest('tr').remove();
        var table = document.getElementById("added_events");

        if ( table.rows.length == 1){
            $('#added_events').hide()
        }
    })

    


});