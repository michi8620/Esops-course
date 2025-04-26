# Esops-course
This is a course for Barista team.

What is SRE? What technologies do we use?:
https://docs.google.com/presentation/d/14lZw6EWNdbgEsl14Lg7Vtc6gwGIbPTeOR_QTC_Su2cY/edit?usp=sharing

## a simple diagram of our monitoring stack:
     ┌──────────────┐
     │  Blackbox    │
     │ Exporter     │
     └────┬─────────┘
          │                         
          ▼                         
     ┌──────────────┐     ┌────────────────┐     ┌────────────┐
     │ Kube State   │     │ Your App (x3)  │<───▶│ OpenTelemetry │
     │ Metrics      │     │  - Logs        │     │ Collector     │
     └────┬─────────┘     │  - Metrics     │     └────┬───────┘
          │               │  - Traces      │          │        
          ▼               └────────────────┘          │        
     ┌──────────────┐                                 ▼        
     │ Prometheus   │<──────────────────────────────┘        
     └────┬─────────┘                                
          │                         
          ▼                         
     ┌──────────────┐              
     │    Grafana   │<─────────────┐
     └──────────────┘              │
          ▲                        │
          │                        │
     ┌──────────────┐      ┌───────┴────────┐
     │     Loki     │<─────┤   Tempo (Traces)│
     └──────────────┘      └─────────────────┘

Course explanation:
each team deploys one service.
each team contains 2-3 members.
