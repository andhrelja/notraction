
function toggleActive(id) {
    let ids = ["cars", "drivers", "events", "championships", "about"];
    for (let li_id of ids) {
        let li = document.getElementById(li_id);
        if (li_id == id) {
            li.classList.toggle("active");
        } else {
            if (li.classList.contains("active")) {
                li.classList.toggle("active");
            }
        }
    }
}
