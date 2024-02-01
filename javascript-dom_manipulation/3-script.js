var click = document.querySelector("#toggle_header");
let currentClass = document.querySelector("header");

click.addEventListener("click", function onClick(event) {
  if (currentClass.classList.contains("red")) {
    currentClass.classList.remove("red");
    currentClass.classList.add("green");
  } else {
    currentClass.classList.remove("green");
    currentClass.classList.add("red");
  }
});
