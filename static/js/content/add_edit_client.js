$(document).ready(function() {

    $("#advanced").click(function() {
        var parent = document.getElementById('advanced')
        var content = document.getElementById('advanced_content')
        var content_status = content.dataset.fieldset_status;

        if (content_status == "open") {
            parent.setAttribute("src", paths['fieldset_close'])
            content.dataset.fieldset_status = 'close';
            $("#advanced_content").slideDown()
        } else {
            parent.setAttribute("src", paths['fieldset_open'])
            content.dataset.fieldset_status = 'open';
            $("#advanced_content").slideUp();
        }

    });
});