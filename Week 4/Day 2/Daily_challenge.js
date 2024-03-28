// Define an array of objects containing information about each planet
const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "brown", moons: 79 },
    { name: "Saturn", color: "yellow", moons: 82 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "blue", moons: 14 }
];

// Function to create a planet div element
function createPlanetDiv(planet) {
    const planetDiv = document.createElement("div");
    planetDiv.classList.add("planet", planet.name.toLowerCase());
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.textContent = planet.name;
    document.querySelector('.listPlanets').appendChild(planetDiv);

    // Add moons if the planet has moons
    if (planet.moons > 0) {
        for (let i = 0; i < planet.moons; i++) {
            const moonDiv = document.createElement("div");
            moonDiv.classList.add("moon");
            moonDiv.style.left = `${Math.random() * 100}%`;
            moonDiv.style.top = `${Math.random() * 100}%`;
            planetDiv.appendChild(moonDiv);
        }
    }
}

// Create planet divs for each planet in the array
planets.forEach(planet => createPlanetDiv(planet));
