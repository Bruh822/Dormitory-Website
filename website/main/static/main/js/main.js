let btnPage = document.getElementById("user-page");
let pages = document.querySelectorAll(".addPages");
btnPage.addEventListener('click', () => {
pages.forEach(elem => {
if (elem.style.display == "inline-block"){
elem.style.display = "none";
}
else{
elem.style.display = "inline-block";
}
})
});