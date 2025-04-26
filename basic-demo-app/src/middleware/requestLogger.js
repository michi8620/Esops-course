const logger = require('../services/logger');

// Middleware to track request timing
function requestLogger(req, res, next) {
  const startTime = Date.now();
  
  logger.info({
    msg: 'Request received',
    method: req.method,
    path: req.path
  });
  
  // Add response tracking
  const originalSend = res.send;
  res.send = function() {
    const responseTime = Date.now() - startTime;
    
    logger.info({
      msg: 'Response sent',
      method: req.method,
      path: req.path,
      statusCode: res.statusCode,
      responseTimeMs: responseTime
    });
    
    return originalSend.apply(res, arguments);
  };
  
  next();
}

module.exports = requestLogger;