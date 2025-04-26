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

## Course explanation:

Each team deploys one service.
In order for each team to get started immediately, each team must deploy their technology along with the ready-made demo app (and other tools if needed).

## team divison: 

otel-collector - Michal
prometheus - Talya and Tamar
kube-state-metrics - yael
loki -Netta
tempo - Shahar
grafana - Roi
blackbox exporter - Amir


