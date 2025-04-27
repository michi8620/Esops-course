import os
import random
import time
import logging
import json
import uuid
from datetime import datetime
from flask import Flask, render_template, jsonify, request

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = Flask(__name__)
logger = logging.getLogger('observability-app')

# List of fictional users for logs
USERS = ["alice", "bob", "charlie", "dave", "eve", "frank", "grace", "heidi"]

# Routes
@app.route('/')
def index():
    """Main page with UI controls"""
    logger.info("Index page accessed")
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    """Simple API endpoint"""
    logger.info("Hello endpoint called")
    return jsonify({"message": "Hello, Observability World!"})

@app.route('/api/compute')
def compute():
    """Endpoint that does some computation - good for resource metrics"""
    # Get complexity parameter (defaults to 1)
    complexity = int(request.args.get('complexity', 1))
    complexity = min(max(complexity, 1), 10)  # Limit between 1-10
    
    logger.info(f"Computing with complexity {complexity}")
    
    # Generate request ID for potential correlation
    request_id = str(uuid.uuid4())
    
    # Simulate work with variable duration based on complexity
    start_time = time.time()
    result = simulate_computation(complexity)
    duration = time.time() - start_time
    
    logger.info(f"Computation completed in {duration:.2f}s with request_id={request_id}")
    return jsonify({
        "request_id": request_id,
        "result": result,
        "complexity": complexity,
        "duration_seconds": duration
    })

@app.route('/api/error')
def error():
    """Endpoint that randomly generates errors"""
    error_rate = float(request.args.get('error_rate', 0.5))
    error_rate = min(max(error_rate, 0), 1)  # Limit between 0-1
    
    request_id = str(uuid.uuid4())
    logger.info(f"Error endpoint called with rate {error_rate}, request_id={request_id}")
    
    if random.random() < error_rate:
        error_type = random.choice(["500", "timeout", "exception"])
        
        if error_type == "500":
            logger.error(f"Simulating a 500 server error, request_id={request_id}")
            return jsonify({"error": "Internal Server Error", "request_id": request_id}), 500
        
        elif error_type == "timeout":
            logger.warning(f"Simulating a slow response, request_id={request_id}")
            time.sleep(random.uniform(1, 5))
            return jsonify({"message": "Response after delay", "request_id": request_id})
        
        else:  # exception
            logger.error(f"Simulating an unhandled exception, request_id={request_id}")
            # This will generate a stack trace in the logs
            1/0  # Intentional division by zero
    
    return jsonify({"message": "No error occurred", "request_id": request_id})

@app.route('/api/logs')
def generate_logs():
    """Generate various types of logs"""
    log_count = int(request.args.get('count', 5))
    log_count = min(max(log_count, 1), 20)  # Limit between 1-20
    
    log_levels = ["debug", "info", "warning", "error"]
    log_weights = [0.4, 0.3, 0.2, 0.1]  # Probability distribution
    
    session_id = str(uuid.uuid4())
    logger.info(f"Generating {log_count} random logs for session {session_id}")
    
    generated_logs = []
    for i in range(log_count):
        level = random.choices(log_levels, weights=log_weights)[0]
        user = random.choice(USERS)
        message = f"User {user} performed action-{i+1} in session {session_id}"
        
        if level == "debug":
            logger.debug(message)
        elif level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
        elif level == "error":
            logger.error(message)
                
        generated_logs.append({
            "level": level,
            "message": message
        })
        
        # Small delay between logs
        time.sleep(0.1)
        
    return jsonify({
        "session_id": session_id,
        "generated_logs": generated_logs
    })

@app.route('/api/users')
def get_users():
    """Endpoints to get user data - generates database-like logs"""
    session_id = str(uuid.uuid4())
    user_count = random.randint(1, len(USERS))
    
    logger.info(f"Fetching {user_count} users in session {session_id}")
    
    # Simulate database query time
    time.sleep(random.uniform(0.05, 0.2))
    
    selected_users = random.sample(USERS, user_count)
    
    # Generate structured log that would be good for querying
    log_data = {
        "session_id": session_id,
        "operation": "user_query",
        "count": user_count,
        "duration_ms": random.randint(50, 200),
        "users": selected_users
    }
    
    logger.info(f"Query completed: {json.dumps(log_data)}")
    
    return jsonify({
        "users": selected_users,
        "session_id": session_id
    })

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

def simulate_computation(complexity):
    """Simulate some CPU-intensive work"""
    result = 0
    iterations = complexity * 1000000
    
    for i in range(iterations):
        result += random.random()
    
    return result / iterations  # Should be close to 0.5

def simulate_background_activity():
    """Generate background activity on a regular basis"""
    while True:
        try:
            # Simulate some backend process
            process_id = str(uuid.uuid4())
            logger.info(f"Background process {process_id} started")
            
            # Simulate various operations
            operations = random.randint(3, 8)
            for i in range(operations):
                op_type = random.choice(["data_sync", "cleanup", "report", "index"])
                duration = random.uniform(0.1, 2.0)
                time.sleep(duration)
                
                if random.random() < 0.1:  # 10% chance of warning
                    logger.warning(f"Slow operation in process {process_id}: {op_type} took {duration:.2f}s")
                else:
                    logger.info(f"Process {process_id} completed operation {op_type} in {duration:.2f}s")
            
            logger.info(f"Background process {process_id} completed")
                
            # Sleep between 5-15 seconds before next batch
            time.sleep(random.uniform(5, 15))
            
        except Exception as e:
            logger.error(f"Error in background process: {str(e)}")
            time.sleep(10)  # Wait before retrying

if __name__ == "__main__":
    # Start background thread for simulated activity
    import threading
    bg_thread = threading.Thread(target=simulate_background_activity, daemon=True)
    bg_thread.start()
    
    # Start the Flask app
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)