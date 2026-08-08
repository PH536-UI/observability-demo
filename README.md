# Cloud Engineering Lab — Observability

Laboratório de observabilidade de uma aplicação Python/FastAPI
executando em Kubernetes, monitorada por Prometheus e Grafana.

## Arquitetura

```text
                    ┌─────────────────────┐
                    │      Grafana        │
                    │    Dashboards       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Prometheus      │
                    │      Scraping       │
                    └──────────┬──────────┘
                               │
                     /metrics  │
                               ▼
              ┌──────────────────────────────┐
              │ Kubernetes - namespace app   │
              │                              │
              │  ┌──────────────┐            │
              │  │ Application  │            │
              │  │   Pod #1     │            │
              │  └──────────────┘            │
              │                              │
              │  ┌──────────────┐            │
              │  │ Application  │            │
              │  │   Pod #2     │            │
              │  └──────────────┘            │
              │                              │
              │       ClusterIP Service      │
              └──────────────────────────────┘
