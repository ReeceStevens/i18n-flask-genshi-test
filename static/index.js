function _(some_str) {
    return some_str
}

document.addEventListener("DOMContentLoaded", function () {
    var p_tag = document.getElementById("add-stuff");
    p_tag.innerText = _("This is some new content");
});
