const apiHandler = {
  calculateExpression: (req, res) => {
    // Replace this with your actual logic for handling the API request
    const { expression } = req.body;

    // Example: Perform some calculation
    const result = eval(expression);

    res.json({ result });
  },
};

module.exports = apiHandler;
