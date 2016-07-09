

$(document).ready(function () {
    var keywords = ["pure", "公司"];
    mark_keywords(keywords);


});

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