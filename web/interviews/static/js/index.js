
$(document).ready(function () {


    
    $('#form-search').submit(function () {
        var wd = $('#form-search .form-control').val();
        return wd != "";
    });

    $('#i-search').click(function () {
        $('#form-search').submit();
    });




});