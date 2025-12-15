const loginForm = document.getElementById("loginForm");
const loginButton = document.getElementById("loginFormSubmit");

var user = [["admin","8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"],["user1","0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e"],[ "user2","6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4"]]
var hashedpassword = "Temp"

//Found hash function at: https://remarkablemark.org/blog/2021/08/29/javascript-generate-sha-256-hexadecimal-hash/
function hash(string) {
  const utf8 = new TextEncoder().encode(string);
  return crypto.subtle.digest('SHA-256', utf8).then((hashBuffer) => {
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray
      .map((bytes) => bytes.toString(16).padStart(2, '0'))
      .join('');
    return hashHex;
  });
}

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    var password = loginForm.password.value;
    hash(password).then(result=>{
        hashedpassword=result
    for (var x=0;x<user.length;x++) {
        if (username===user[x][0] && hashedpassword===user[x][1]){
            alert("You have successfully logged in.");
            chrome.action.setPopup({popup: 'main.html'});
            location.assign("main.html");
            break;
        }   
        else{
            if (x==(user.length-1)){
                alert("You have entered the wrong username or password.")
            }
        }
    }
})
})
