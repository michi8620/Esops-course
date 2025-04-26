mode: deployment

config:
  exporters:
    logging:
      loglevel: debug
  service:
    pipelines:
      logs:
        receivers: [otlp]
        processors: []
        exporters: [logging]
      metrics:
        receivers: [otlp]
        processors: []
        exporters: [logging]
      traces:
        receivers: [otlp]
        processors: []
        exporters: [logging]

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 200m
    memory: 256Mi
