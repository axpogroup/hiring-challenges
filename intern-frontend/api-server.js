// Simple Mock API Server for the Weather Challenge
const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// Mock weather data - 100 European cities
const cities = [
  "London",
  "Paris",
  "Berlin",
  "Madrid",
  "Rome",
  "Amsterdam",
  "Vienna",
  "Prague",
  "Budapest",
  "Warsaw",
  "Stockholm",
  "Copenhagen",
  "Oslo",
  "Helsinki",
  "Dublin",
  "Brussels",
  "Lisbon",
  "Athens",
  "Bucharest",
  "Sofia",
  "Zagreb",
  "Belgrade",
  "Bratislava",
  "Ljubljana",
  "Tallinn",
  "Riga",
  "Vilnius",
  "Luxembourg",
  "Monaco",
  "Zurich",
  "Geneva",
  "Basel",
  "Bern",
  "Lausanne",
  "Milan",
  "Venice",
  "Florence",
  "Naples",
  "Turin",
  "Bologna",
  "Barcelona",
  "Valencia",
  "Seville",
  "Bilbao",
  "Oporto",
  "Marseille",
  "Lyon",
  "Toulouse",
  "Nice",
  "Bordeaux",
  "Hamburg",
  "Munich",
  "Frankfurt",
  "Cologne",
  "Stuttgart",
  "Dusseldorf",
  "Leipzig",
  "Dresden",
  "Manchester",
  "Liverpool",
  "Birmingham",
  "Leeds",
  "Glasgow",
  "Edinburgh",
  "Bristol",
  "Rotterdam",
  "The Hague",
  "Utrecht",
  "Eindhoven",
  "Antwerp",
  "Ghent",
  "Bruges",
  "Krakow",
  "Gdansk",
  "Wroclaw",
  "Poznan",
  "Gothenburg",
  "Malmo",
  "Uppsala",
  "Bergen",
  "Trondheim",
  "Stavanger",
  "Tampere",
  "Turku",
  "Espoo",
  "Cork",
  "Galway",
  "Limerick",
  "Porto",
  "Braga",
  "Coimbra",
  "Valencia",
  "Granada",
  "Palma",
  "Alicante",
  "Salzburg",
  "Innsbruck",
  "Graz",
  "Linz",
  "Baden",
];

const conditions = [
  "Sunny",
  "Cloudy",
  "Rainy",
  "Windy",
  "Foggy",
  "Snowy",
  "Partly Cloudy",
];

const weatherData = cities.map((city, index) => ({
  id: index + 1,
  city: city,
  temperature: Math.floor(Math.random() * 30) + 5, // Random temp between 5-35°C
  condition: conditions[Math.floor(Math.random() * conditions.length)],
  humidity: Math.floor(Math.random() * 60) + 30, // Random humidity between 30-90%
}));

// GET endpoint to fetch weather data
app.get("/weather", (req, res) => {
  // Simulate network delay
  setTimeout(() => {
    res.json(weatherData);
  }, 500);
});

app.listen(PORT, () => {
  console.log(`✅ Mock API server running at http://localhost:${PORT}`);
  console.log(`📡 Weather endpoint: http://localhost:${PORT}/weather`);
});
