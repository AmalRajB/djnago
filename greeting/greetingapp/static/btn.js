let h1 = document.getElementsByTagName('h4')[0];
const btn = document.getElementById('btn');
btn.addEventListener("click", function() {
    h1.innerHTML = "this is home page";
});