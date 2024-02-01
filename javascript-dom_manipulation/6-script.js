const currentClass = document.querySelector("#character");
async function logname() {
  try {
    const response = await fetch(
      "https://swapi-api.hbtn.io/api/people/5/?format=json"
    );
    const data = await response.json();
    const characterName = data.name;
    currentClass.textContent = characterName;
    console.log(characterName);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

logname();
