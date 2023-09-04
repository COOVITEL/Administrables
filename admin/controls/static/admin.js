var button1 = document.querySelector('.bt1');
var button2 = document.querySelector('.bt2');
var login = document.querySelector('.login');
var register = document.querySelector('.register');

button1.addEventListener("click", function() {
    button1.classList.add("act")
    button2.classList.remove("act")
    login.classList.add("see")
    register.classList.remove("see")
})

button2.addEventListener("click", function() {
    button2.classList.add("act")
    button1.classList.remove("act")
    register.classList.add("see")
    login.classList.remove("see")
})
