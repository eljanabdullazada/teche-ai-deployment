from fastapi import FastAPI

app = FastAPI(title="AI Starter Kit Backend")

@app.get("/health")
def health():
    return {
        "wlms": "Welcome July 13 test 1"
    }
