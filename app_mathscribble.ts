// TypeScript App Logic for MathScribble

import { API_BASE_URL, DEBUG_MODE } from "./config_mathscribble";

class MathScribbleApp {
  private apiBaseUrl: string;

  constructor(apiBaseUrl: string) {
    this.apiBaseUrl = apiBaseUrl;
  }

  fetchData(endpoint: string): Promise<any> {
    const apiUrl = `${this.apiBaseUrl}/${endpoint}`;

    // Implement your data fetching logic using fetch or a library like axios
    return fetch(apiUrl)
      .then((response) => response.json())
      .catch((error) => {
        if (DEBUG_MODE) {
          console.error("Error fetching data:", error);
        }
        throw error;
      });
  }

  // Add more app logic as needed
}

// Instantiate MathScribbleApp
const mathScribbleApp = new MathScribbleApp(API_BASE_URL);

// Example usage
mathScribbleApp
  .fetchData("calculate")
  .then((data) => {
    console.log("Calculation result:", data);
    // Handle the data as needed
  })
  .catch((error) => {
    console.error("Error:", error);
    // Handle errors
  });
