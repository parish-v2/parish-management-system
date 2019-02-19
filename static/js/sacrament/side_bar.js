function nav_item_click(id){
    var elem = document.getElementById(id);
    var nav_bar = elem.parentElement
    for (var i = 0; i < nav_bar.children.length; i++) {
        // children[i].classList.add("");
        children[i].classList.remove("active");
    }
    elem.classList.add("active")
}

