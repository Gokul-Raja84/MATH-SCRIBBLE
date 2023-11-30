package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	// Initialize router
	router := mux.NewRouter()

	// Define routes
	router.HandleFunc("/", homeHandler).Methods("GET")
	router.HandleFunc("/calculate", calculateHandler).Methods("POST")

	// Start the server
	port := 8080
	fmt.Printf("MathScribble server is running on http://localhost:%d\n", port)
	http.ListenAndServe(fmt.Sprintf(":%d", port), router)
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Welcome to MathScribble!")
}

func calculateHandler(w http.ResponseWriter, r *http.Request) {
	// Add logic for handling calculation requests
	// Example: Parse JSON payload, perform calculation, and send response
	fmt.Fprint(w, "Calculation result will be sent here...")
}
