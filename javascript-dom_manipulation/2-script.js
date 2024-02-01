var click = document.querySelector("#red_header");
let currentClass = document.querySelector("header");
click.addEventListener("click", function onClick(event) {
  currentClass.classList.add("red");
});
