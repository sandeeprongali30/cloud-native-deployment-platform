from fastapi import FastAPI
import os

app = FastAPI(title="Cloud Native Deployment API")

# Version (comes from environment variable)
APP_VERSION = os.getenv("APP_VERSION", "v1")

# Pod name (important for Kubernetes visibility)
POD_NAME = os.getenv("HOSTNAME", "unknown")

# Simple request counter
request_count = 0


@app.get("/")
def root():
    global request_count
    request_count += 1

    return {
        "message": "Deployment Platform API",
        "version": APP_VERSION,
        "pod": POD_NAME,
        "request_count": request_count
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "pod": POD_NAME
    }