
$(document).ready(function () {


    
    $('#form-search').submit(function () {
        var wd = $('#form-search .form-control').val();
        // $('#form-search .form-control').val(encodeURI(wd));
        return wd != "";
    });

    $('#i-search').click(function () {
        $('#form-search').submit();
    });
    

});

function httpGet(theUrl, wd) {

    wd = encodeURI(wd);
    // var url = window.location.href;     // Returns full URL

    var p = {
        wd: wd
    }
    var target = theUrl + "?" + $.param(p)

    window.location.href = target;
}