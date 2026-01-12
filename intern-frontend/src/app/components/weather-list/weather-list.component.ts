import { Component, signal, effect, inject } from "@angular/core";
import { CommonModule } from "@angular/common";
import { WeatherService } from "../../services/weather.service";
import { Weather } from "../../models/weather.model";

@Component({
  selector: "app-weather-list",
  standalone: true,
  imports: [CommonModule],
  templateUrl: "./weather-list.component.html",
  styleUrls: ["./weather-list.component.css"],
})
export class WeatherListComponent {
  /**
   * TODO: Task 2 - Complete this component
   *
   * Instructions:
   * 1. Create signals to store:
   *    - weatherData
   *
   * Hint: Use signal() to create reactive state
   * Example: mySignal = signal<Type>(initialValue);
   *
   * 2. Service injection using modern inject() function
   *
   * 3. Use the effect to call the weather service and fetch data:
   *    - Subscribe to the observable from getWeather()
   *    - Update weatherData signal with the response
   *
   * Hint: Use untracked(() => {})
   */
  //  TODO: Service injection using modern inject() function
  // TODO: Create signals here
  // TODO: Implement data fetching logic here
  // Hint:
  // 1. Set isLoading to true: this.isLoading.set(true)
  // 2. Call this.weatherService.getWeather().subscribe({ ... })
  // 3. In next: update weatherData signal
  // 4. In error: update errorMessage signal
  // 5. In complete: set isLoading to false
  //  TODO: EXTRA - implement data loading and error handling
}
