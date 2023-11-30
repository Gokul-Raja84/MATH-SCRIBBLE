// General utility functions

const capitalize = (str) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
};

const formatDate = (date) => {
  // Add logic for formatting date
  return date.toISOString();
};

export { capitalize, formatDate };
