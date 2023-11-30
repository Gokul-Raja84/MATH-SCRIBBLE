// API route handling

const express = require("express");
const { getUserById, updateUser } = require("./apiHandler");

const router = express.Router();

// Define API routes
router.get("/user/:id", async (req, res) => {
  const userId = req.params.id;

  try {
    const user = await getUserById(userId);
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
});

router.put("/user/:id", async (req, res) => {
  const userId = req.params.id;
  const updateData = req.body;

  try {
    const updatedUser = await updateUser(userId, updateData);
    res.json(updatedUser);
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
});

module.exports = router;
