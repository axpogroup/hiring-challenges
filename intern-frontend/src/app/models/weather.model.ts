// TODO: Define the Weather interface based on the API response example below
// The API returns data in this format:

// Example API Response:
// {
//   "id": 1,
//   "city": "London",
//   "temperature": 15,
//   "condition": "Cloudy",
//   "humidity": 65
// }

export interface Weather {
  id: any;
  city: any;
  temperature: any;
  condition: any;
  humidity: any;
}
