// Utility functions for AJAX requests

const fetchData = (url, options) => {
  // Implement AJAX request logic using fetch or XMLHttpRequest
  return fetch(url, options)
    .then((response) => response.json())
    .catch((error) => console.error("Error fetching data:", error));
};

export { fetchData };
