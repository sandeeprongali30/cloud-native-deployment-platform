# Cloud-Native Deployment Platform

## Overview

This project demonstrates a cloud-native deployment platform designed to automate application delivery using Kubernetes, GitOps, and CI/CD practices.

It supports multi-environment deployments (dev, stage, prod) using declarative configurations and modern DevOps tooling.

## Key Features

- Kubernetes-based deployments
- GitOps workflow using FluxCD
- Helm templating for reusable deployments
- CI/CD pipeline integration
- Multi-environment support

## Tech Stack

- Kubernetes
- Helm
- FluxCD
- FastAPI
- Docker
- GitHub Actions
- Prometheus & Grafana

## Project Structure

- api/ --> Deployment service
- helm/ --> Helm charts
- gitops/ --> GitOps configs
- environments/ --> Environment-specific configs
- monitoring/ --> Observability stack

## Status

Initial setup in progress
