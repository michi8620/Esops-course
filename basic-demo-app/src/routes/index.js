const express = require('express');
const router = express.Router();

// Root endpoint
router.get('/', (req, res) => {
  res.send({ message: 'Demo API is running!' });
});

module.exports = router;