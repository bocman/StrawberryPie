$(document).ready(function () {
    $('input[name="change_passwords"]').click(function() {
        if ( $(this).prop('checked') ) {
            $("#id_password").show()
            $('label[for="id_password"]').show()
            $("#id_confirm_password").show()
            $('label[for="id_confirm_password"]').show()

        }
        else{
            $("#id_password").hide()
            $('label[for="id_password"]').hide()
            $("#id_confirm_password").hide()
            $('label[for="id_confirm_password"]').hide()
        }
    });
});