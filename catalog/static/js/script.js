function showMenu() {
    let sidebar_nav = document.getElementsByClassName("sidebar-nav").item(0);
    let side_menu = document.getElementsByClassName("sidebar").item(0);

    if (sidebar_nav.classList.contains("hidden")) {
        sidebar_nav.classList.remove("hidden");
        side_menu.classList.remove("tight");
        side_menu.classList.add("wide");
    } else {
        sidebar_nav.classList.add("hidden");
        side_menu.classList.add("tight");
        side_menu.classList.remove("wide");
    }

}

let open_menu_button = document.getElementById("open-menu-button");
open_menu_button.onclick = showMenu;
