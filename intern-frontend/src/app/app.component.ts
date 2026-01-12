import { Component } from "@angular/core";
import { WeatherListComponent } from "./components/weather-list/weather-list.component";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [WeatherListComponent],
  template: `
    <div class="app-container">
      <h1>🌤️ Weather Dashboard</h1>
      <app-weather-list></app-weather-list>
    </div>
  `,
  styles: [
    `
      .app-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
      }
    `,
  ],
})
export class AppComponent {
  title = "Weather Dashboard";
}
