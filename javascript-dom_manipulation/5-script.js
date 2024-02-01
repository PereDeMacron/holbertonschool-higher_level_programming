var click = document.querySelector("#update_header");
let currentClass = document.querySelector("header");

click.addEventListener("click", function onClick(event) {
  currentClass.textContent = "New Header!!!";
});
