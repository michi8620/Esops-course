# Basic Demo Application for OpenTelemetry Learning

This is a structured Express.js application designed for learning OpenTelemetry instrumentation.
The app has no OpenTelemetry instrumentation yet - that's your task!

## Project Structure

```
basic-demo-app/
├── package.json        - Dependencies and scripts
├── README.md           - This documentation
├── Dockerfile          - For containerized deployment
├── src/                - Source code
│   ├── server.js       - Application entry point
│   ├── middleware/     - Express middleware
│   ├── routes/         - API route definitions
│   └── services/       - Shared services
└── docker-compose.yml  - Container orchestration
```

## Features

The application provides several endpoints that simulate different scenarios:

- `GET /`: Basic health check endpoint
- `GET /error`: Generates an error to demonstrate error tracking
- `GET /slow`: Endpoint with a 2-second delay to demonstrate latency tracking
- `GET /external`: Makes an external API call
- `GET /database`: Simulates a database query with variable response time
- `GET /compute`: Performs a CPU-intensive calculation
- `GET /chain`: Executes a chain of operations with occasional failures

## Getting Started

1. Install dependencies:
   ```
   npm install
   ```

2. Run the application:
   ```
   npm start
   ```

3. Access the application at http://localhost:3000

## Your Task

Add OpenTelemetry instrumentation to this application to collect:
- Metrics
- Logs
- Traces

You'll need to:
1. Add appropriate OpenTelemetry dependencies
2. Create instrumentation configuration
3. Set up an OpenTelemetry Collector
4. Configure exporters to view the telemetry data

## Learning Goals

- Understand how to instrument a Node.js application with OpenTelemetry
- Learn how to configure auto-instrumentation for common libraries
- Practice adding custom spans, metrics, and attributes
- Configure an OpenTelemetry Collector
- Connect your telemetry pipeline to visualization and analysis tools

## Next Steps

After instrumenting the application, explore:
- How different operations appear in traces
- How errors are captured
- How external calls are tracked
- Performance metrics for different endpoints