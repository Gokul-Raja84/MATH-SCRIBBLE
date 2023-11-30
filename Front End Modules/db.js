// Database connection setup

const mongoose = require("mongoose");

const connectToDatabase = () => {
  const dbUrl = "mongodb://localhost:27017/your_database_name";

  mongoose.connect(dbUrl, { useNewUrlParser: true, useUnifiedTopology: true });
  const db = mongoose.connection;

  db.on("error", console.error.bind(console, "MongoDB connection error:"));
  db.once("open", () => {
    console.log("Connected to the database");
  });
};

module.exports = connectToDatabase;
