const DARK_MODE_TOGGLE = document.querySelector("#dark-mode-toggle")
const LIGHT_MODE_TOGGLE = document.querySelector("#light-mode-toggle")

// EFFECTS: sends a POST request to the route "/deleteNote", then the response is to redirect home
function deleteNote(noteId) {
    fetch("/delete-note", 
    {method: "POST",
    body: JSON.stringify({noteId: noteId})}).then((_res) => {
    window.location.href= "/"; // redirect to home
});   
}

// EFFECTs: todo
function toggleLightMode() {
    console.log("clicked");
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.removeItem("darkMode");
}

// EFFECTs: todo
function toggleDarkMode() {
    console.log("clicked");
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("darkMode", "enabled");
}

function checkDarkMode() {
    if (localStorage.getItem("darkMode") !== "enabled"){ // if key:value pair DNE already
        toggleDarkMode();
    }
}

// EFFECTs: todo
DARK_MODE_TOGGLE.addEventListener("click", () => {
    checkDarkMode();
})

// EFFECTs: todo
LIGHT_MODE_TOGGLE.addEventListener("click", () => {
    if (localStorage.getItem("darkMode") == "enabled"){
        toggleLightMode();
    }
})

// EFFECTs: todo
window.addEventListener("load", console.log(localStorage.getItem("darkMode")));
window.addEventListener("load", () => {
    if (localStorage.getItem("darkMode") === "enabled") {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    }
});



