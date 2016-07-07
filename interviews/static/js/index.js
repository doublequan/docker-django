
$(document).ready(function () {
    $(".jq-test").html("Context by <b>JS</b>");

    $("#btn-click").click(function () {
        // $(".jq-test").toggle(500);
        // $(".jq-test").fadeToggle(500);
        $(".jq-test").slideToggle(500);
    });

    $('#btn-search').click(function () {
        window.location.href="newest/";
    });


});