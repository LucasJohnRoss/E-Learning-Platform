const InfoButton = document.getElementById("InfoButton");
const WebAppButton = document.getElementById("WebAppButton");
const LogOutButton = document.getElementById("LogOutButton");

InfoButton.addEventListener("click",(e) => {
    e.preventDefault();
    location.assign("info.html");
});
WebAppButton.addEventListener("click", (e) => {
    e.preventDefault();
    chrome.tabs.update({url:"http://127.0.0.1:5000/login"});
});
LogOutButton.addEventListener("click", (e) => {
    e.preventDefault();
    chrome.action.setPopup({popup: 'login.html'});
    location.assign("login.html");
});
