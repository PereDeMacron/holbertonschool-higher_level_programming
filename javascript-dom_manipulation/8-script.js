const currentClass = document.querySelector("#hello");
async function logname() {
  try {
    const response = await fetch(
      "https://hellosalut.stefanbohacek.dev/?lang=fr"
    );
    const data = await response.json();
    const value = data.hello;
    currentClass.textContent = value;
    console.log(value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

logname();
