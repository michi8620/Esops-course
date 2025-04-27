# Observability Learning Application

A simple application designed for learning various observability technologies in Kubernetes/OpenShift environments.

## Application Overview

This is a simple Flask application that:

1. **Generates activity without any built-in monitoring instrumentation:**
   - Standard application logs (not using OpenTelemetry)
   - HTTP endpoints with varying performance characteristics
   - CPU-intensive operations
   - Error conditions
   - Background processes that generate activity

2. **Includes useful patterns for monitoring:**
   - Request IDs in logs and responses for correlation
   - Session IDs for grouping related operations
   - Structured logging that can be parsed
   - Varying error rates and response times
   - Resource-intensive operations

3. **Simple UI to trigger activities:**
   - Buttons to generate different types of requests
   - Controls for log volume, error rates, and computational complexity

## Supported Observability Technologies

This application is designed to be monitored using:

- OpenTelemetry Collector
- Prometheus
- Loki
- Tempo
- Blackbox Exporter
- Kube State Metrics

## Deployment Instructions

To deploy this application in OpenShift's sandbox:

1. Build the Docker image:
   ```bash
   docker build -t observability-app:latest .
   ```

2. Push to your container registry:
   ```bash
   docker tag observability-app:latest <registry>/observability-app:latest
   docker push <registry>/observability-app:latest
   ```

3. Deploy using the Helm chart:
   ```bash
   helm install obs-app ./helm --set image.repository=<registry>/observability-app
   ```

## Learning Opportunities

With this application, you can learn how to:

1. **Set up Prometheus scraping** to monitor:
   - HTTP request counts and latencies
   - Error rates
   - Resource usage (CPU, memory)
   - Custom application metrics

2. **Configure Loki** to:
   - Collect and parse the application logs
   - Create queries to find errors
   - Set up log aggregation
   - Correlate logs using request IDs

3. **Implement Tempo** for:
   - Distributed tracing without built-in instrumentation
   - Correlating logs and traces

4. **Use Blackbox Exporter** to:
   - Monitor endpoints from outside the application
   - Track availability and response times

5. **Configure Kube State Metrics** to:
   - Monitor the health of the application's pods
   - Track deployments and replica status

## Project Structure

```
observability-app/
├── main.py                  # Main application code
├── templates/               # HTML templates for UI
│   └── index.html
├── Dockerfile               # Container definition
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── .gitignore               # Git ignore file
└── helm/                    # Helm chart for deployment
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        ├── route.yaml       # OpenShift route
        └── _helpers.tpl
```

## Application Endpoints

- `/` - Main UI for triggering various activities
- `/api/hello` - Simple endpoint that returns a greeting
- `/api/compute` - CPU-intensive endpoint with variable complexity
- `/api/error` - Endpoint that generates errors at a configurable rate
- `/api/logs` - Generates a configurable number of log messages
- `/api/users` - Simulates a database query with variable results
- `/api/health` - Health check endpoint