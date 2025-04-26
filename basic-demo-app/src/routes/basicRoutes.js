const express = require('express');
const axios = require('axios');
const logger = require('../services/logger');

const router = express.Router();

// Root endpoint
router.get('/', (req, res) => {
  res.send({ message: 'Demo API is running!' });
});

// Endpoint to generate errors for error tracking
router.get('/error', (req, res) => {
  logger.error('This is an example error!');
  
  // Create an error but catch it for demonstration
  try {
    throw new Error('Example error for demo purposes');
  } catch (e) {
    res.status(500).send({ error: 'Intentional error generated' });
  }
});

// Endpoint with artificial delay to demonstrate latency tracking
router.get('/slow', async (req, res) => {
  logger.info('Starting slow operation');
  
  // Simulate a slow operation
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  logger.info('Slow operation completed');
  res.send({ message: 'Slow operation completed' });
});

// Endpoint to make an external HTTP call
router.get('/external', async (req, res) => {
  try {
    logger.info('Making external API call');
    const response = await axios.get('https://jsonplaceholder.typicode.com/todos/1');
    res.send({ 
      message: 'External API call completed',
      data: response.data
    });
  } catch (error) {
    logger.error('External API call failed', error);
    res.status(500).send({ error: 'External API call failed' });
  }
});

module.exports = router;