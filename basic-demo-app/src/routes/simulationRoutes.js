const express = require('express');
const logger = require('../services/logger');

const router = express.Router();

// Database simulation with artificial latency
router.get('/database', async (req, res) => {
  logger.info('Simulating database query');
  
  // Simulate database operation time
  const dbOperationTime = Math.floor(Math.random() * 500) + 100;
  await new Promise(resolve => setTimeout(resolve, dbOperationTime));
  
  const results = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' }
  ];
  
  logger.info({
    msg: 'Database query completed',
    timeMs: dbOperationTime,
    resultCount: results.length
  });
  
  res.send({
    message: 'Database query successful',
    queryTimeMs: dbOperationTime,
    results
  });
});

// CPU intensive operation to demonstrate performance tracking
router.get('/compute', (req, res) => {
  logger.info('Starting CPU intensive operation');
  
  const startTime = Date.now();
  
  // Simulate CPU intensive operation
  let result = 0;
  for (let i = 0; i < 10000000; i++) {
    result += Math.sqrt(i);
  }
  
  const duration = Date.now() - startTime;
  
  logger.info({
    msg: 'CPU intensive operation completed',
    durationMs: duration
  });
  
  res.send({
    message: 'Computation completed',
    durationMs: duration,
    result: result.toFixed(2)
  });
});

// Endpoint with a chain of operations
router.get('/chain', async (req, res) => {
  logger.info('Starting operation chain');
  
  // First operation
  await new Promise(resolve => setTimeout(resolve, 300));
  logger.info('First operation completed');
  
  // Second operation
  await new Promise(resolve => setTimeout(resolve, 500));
  logger.info('Second operation completed');
  
  // Third operation - sometimes fails
  const shouldFail = Math.random() < 0.3;
  if (shouldFail) {
    logger.error('Third operation failed');
    res.status(500).send({ error: 'Random failure in operation chain' });
    return;
  }
  
  // Complete chain
  logger.info('Operation chain completed successfully');
  res.send({ message: 'Chain of operations completed' });
});

module.exports = router;