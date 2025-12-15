const BackButton = document.getElementById("BackButton");

BackButton.addEventListener("click", (e) => {
    e.preventDefault();
    location.assign("main.html");
})

