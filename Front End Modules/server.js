const express = require("express");
const bodyParser = require("body-parser");
const routes = require("./routes");

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Setup routes
app.use("/api", routes);

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
