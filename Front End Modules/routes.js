const express = require("express");
const apiHandler = require("./apiHandler");

const router = express.Router();

// Define routes
router.post("/calculate", apiHandler.calculateExpression);

module.exports = router;
