const DARK_MODE_TOGGLE = document.querySelector("#dark-mode-toggle");
const LIGHT_MODE_TOGGLE = document.querySelector("#light-mode-toggle");
const CAT_BUTTON = document.querySelector("#generate-cat");

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
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.removeItem("darkMode");
}

// EFFECTs: todo
function toggleDarkMode() {
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("darkMode", "enabled");
}

function checkDarkMode() {
    if (localStorage.getItem("darkMode") !== "enabled"){ // if key:value pair DNE 
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
window.addEventListener("load", () => {
    if (localStorage.getItem("darkMode") === "enabled") {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    }
});

// EFFECTs:
async function retrieveNewCat() {
    console.log("I have been called!");
    await fetch("https://cataas.com/cat", {cache: 'reload', mode: 'no-cors'})
    document.getElementById("cat-img").src="https://cataas.com/cat";
}





