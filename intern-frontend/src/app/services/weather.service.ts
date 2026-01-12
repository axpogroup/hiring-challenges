import { Injectable, signal } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Weather } from "../models/weather.model";

@Injectable({
  providedIn: "root",
})
export class WeatherService {
  private apiUrl = "http://localhost:3000/weather";

  constructor(private http: HttpClient) {}

  /**
   * TODO: Complete this method to fetch weather data from the API
   *
   * Instructions:
   * 1. Use the HttpClient to make a GET request to this.apiUrl
   * 2. The API returns an array of Weather objects
   * 3. Return the observable from http.get()
   *
   * Hint: Use this.http.get<Weather[]>(this.apiUrl)
   */
  getWeather() {
    // TODO: Implement this method
    // Example: return this.http.get<Weather[]>(this.apiUrl);
    throw new Error("Method not implemented - complete this in Task 1");
  }
}
