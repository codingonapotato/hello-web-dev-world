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

// EFFECTs: updates the HTML to use the light mode version of the website
function toggleLightMode() {
    document.documentElement.setAttribute("data-bs-theme", "light");
    localStorage.removeItem("darkMode");
}

// EFFECTs: updates the HTML to use the dark mode version of the website
function toggleDarkMode() {
    document.documentElement.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("darkMode", "enabled");
}

// EFFECTs: toggles darkmode if darkmode is not already enabled
function checkDarkMode() {
    if (localStorage.getItem("darkMode") !== "enabled"){ // if key:value pair DNE already
        toggleDarkMode();
    }
}

// EFFECTs: calls checkDarkMode() when the dark mode button is clicked by the user
DARK_MODE_TOGGLE.addEventListener("click", () => {
    checkDarkMode();
})

// EFFECTs: calls toggleLightMode() when the light mode button is clicked by the user 
// and if darkMode was enabled
LIGHT_MODE_TOGGLE.addEventListener("click", () => {
    if (localStorage.getItem("darkMode") == "enabled"){
        toggleLightMode();
    }
})

// EFFECTs: upon loading of the webapge, this checks to see if the user had 
// previouly selected preference for dark mode on a previous visit
window.addEventListener("load", () => {
    if (localStorage.getItem("darkMode") === "enabled") {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    }
});

// EFFECTs: retrieves a new cat image every time the button with id="cat-img" 
// is clicked and updates the src field with the link to the image.
async function retrieveNewCat() {
    console.log("I have been called!");
    await fetch("https://cataas.com/cat", {cache: 'reload', mode: 'no-cors'})
    document.getElementById("cat-img").src="https://cataas.com/cat";
}





