

$(document).ready(function () {

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


function content_toggle(a) {
    if (a.text == "Show All") {
        $(a).prevAll(".content-desc-all").show();
        $(a).prevAll(".content-desc-partial").hide();
        a.text = "Hide";
    } else {
        $(a).prevAll(".content-desc-all").hide();
        $(a).prevAll(".content-desc-partial").show();
        a.text = "Show All";
        // window.location.href = ("#" + a.title);
    }

}


function mark_keywords(keywords) {
    if (keywords.length == 0) return;
    var pattern = "(" + keywords[0] + ")";
    for (var i = 1; i < keywords.length; i++) {
        pattern += "|(" + keywords[i] + ")";
    }
    console.log(pattern);
    var regex = new RegExp(pattern, "g")

    var title = $(".content-title").html().replace(regex, "<em>$&</em>");
    $(".content-title").html(title);

    var desc = $(".content-desc").html().replace(regex, "<em>$&</em>");
    $(".content-desc").html(desc);

}