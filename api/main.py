from fastapi import FastAPI

app = FastAPI(title="Deployment API")

@app.get("/")
def root():
    return {"message": "Deployment Platform API is running"}

@app.post("/deploy")
def deploy(config: dict):
    return {
        "status": "deployment request received",
        "config": config
    }