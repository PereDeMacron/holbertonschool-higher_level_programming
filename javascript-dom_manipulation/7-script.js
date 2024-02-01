const currentClass = document.querySelector("#list_movies");

async function fetchAndListMovies() {
  try {
    const response = await fetch(
      "https://swapi-api.hbtn.io/api/films/?format=json"
    );
    const data = await response.json();
    const movies = data.results;
    currentClass.innerHTML = "";
    movies.forEach((movie) => {
      const listItem = document.createElement("li");
      listItem.textContent = movie.title;
      currentClass.appendChild(listItem);
    });
  } catch (error) {
    console.error("Error fetching and listing movies:", error);
  }
}

fetchAndListMovies();
