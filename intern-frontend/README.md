# Frontend Intern Challenge - Weather Dashboard

**Time limit: 25 minutes**

## Overview

Build a simple weather dashboard that displays current weather information for different cities using a public API.

## What We're Testing

- Basic TypeScript knowledge
- Understanding of REST API integration
- Modern Angular patterns (signals, control flow)
- Basic HTML/CSS skills
- Problem-solving approach
- Clean, readable code

## The Challenge

You need to complete a weather dashboard application that:

1. Fetches weather data from a mock API endpoint
2. Displays the weather information in cards
3. Shows loading states while fetching data
4. Handles errors gracefully

## Setup Instructions

1. Install dependencies:

```bash
npm install
```

2. Start the development server:

```bash
npm start
```

3. Start the mock API server (in a separate terminal):

```bash
npm run api
```

The app will run at `http://localhost:4200`
The API will run at `http://localhost:3000`

## Your Tasks

### Task 1: Setup Types and Service (15 min)

**Step 1: Fix the Weather Model**
**File: `src/app/models/weather.model.ts`**

- Review the API response example in the comments
- Fix the interface types (currently all set to `any`)
- Use proper TypeScript types based on the data

**Step 2: Complete the Weather Service**
**File: `src/app/services/weather.service.ts`**

Complete the `getWeather()` method to:

- Make an HTTP GET request to `http://localhost:3000/weather`
- Return the Observable from the HTTP call
- The API returns an array of Weather objects

### Task 2: Display Weather Cards (8 min)

**File: `src/app/components/weather-list/weather-list.component.ts` and `.html`**

- Subscribe to the weather service in the component
- Use signals to manage state (weatherData, isLoading, errorMessage)
- Display each city's weather in a card showing:
  - City name
  - Temperature
  - Weather condition (e.g., "Sunny", "Rainy")
  - Humidity percentage
- Show a loading message while data is being fetched
- Show an error message if the request fails
- Use modern Angular control flow syntax (@if, @for)
- Remember to call signals with () in the template

### Task 3: Basic Styling (2 min)

**File: `src/app/components/weather-list/weather-list.component.css`**

Add basic styling to make the cards look presentable:

- Display cards in a grid/flex layout
- Add padding and margins
- Use different colors for different weather conditions (optional)

## API Response Format

```json
[
  {
    "id": 1,
    "city": "London",
    "temperature": 15,
    "condition": "Cloudy",
    "humidity": 65
  },
  {
    "id": 2,
    "city": "Paris",
    "temperature": 18,
    "condition": "Sunny",
    "humidity": 45
  }
]
```

## What You Can Use

- ✅ Angular documentation
- ✅ TypeScript documentation
- ✅ AI assistance (ChatGPT, Copilot, etc.)
- ✅ Stack Overflow / Online resources

## Evaluation Criteria

We're looking for:

1. **Functionality** - Does it work?
2. **Code Quality** - Is the code readable and organized?
3. **Problem Solving** - How do you approach the problem?
4. **Basic Knowledge** - Do you understand TypeScript types, async operations, and HTTP calls?

## Bonus Points (Optional)

If you finish early, try to add:

- A refresh button to reload weather data
- Temperature unit toggle (Celsius/Fahrenheit)
- Search/filter cities by name

## Submission

Once completed, ensure your app runs without errors and displays the weather data correctly.

Good luck! 🚀
