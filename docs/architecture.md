# Architecture

## Overview

This project demonstrates a simple cloud-native observability stack.

The application runs as a containerized Python service deployed on Kubernetes.

Prometheus collects application metrics and Grafana provides visualization and monitoring.

## Architecture

```text
                    ┌──────────────────────┐
                    │      Developer       │
                    │       GitHub         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Docker          │
                    │    Python Image      │
                    └──────────┬───────────┘
                               │
                               ▼
                 ┌───────────────────────────┐
                 │       Kubernetes          │
                 │                           │
                 │  ┌─────────────────────┐  │
                 │  │   Python App        │  │
                 │  │                     │  │
                 │  │   /metrics          │  │
                 │  └──────────┬──────────┘  │
                 │             │             │
                 └─────────────┼─────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Prometheus       │
                    │   Metrics Collector  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Grafana        │
                    │    Visualization     │
                    └──────────────────────┘
