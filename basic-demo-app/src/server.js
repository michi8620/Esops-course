const express = require('express');
const logger = require('./services/logger');
const requestLogger = require('./middleware/requestLogger');
const basicRoutes = require('./routes/basicRoutes');
const simulationRoutes = require('./routes/simulationRoutes');

// Create the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Apply middleware
app.use(requestLogger);

// Register routes
app.use('/', basicRoutes);
app.use('/', simulationRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  logger.error({
    msg: 'Unhandled application error',
    error: err.message,
    stack: err.stack
  });
  
  res.status(500).send({
    error: 'Internal Server Error',
    message: err.message
  });
});

// Start the server
app.listen(PORT, () => {
  logger.info(`Server is running on port ${PORT}`);
});

