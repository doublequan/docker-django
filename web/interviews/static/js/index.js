
$(document).ready(function () {


    
    $('#form-search').submit(function () {
        var wd = $('#form-search .form-control').val();
        return wd != "";
    });

    $('#i-search').click(function () {
        $('#form-search').submit();
    });
    

});

function httpGet(theUrl, wd) {
    console.log(theUrl);
    console.log(wd);
    var p = {
        wd: wd
    }
    console.log($.param(p));
}