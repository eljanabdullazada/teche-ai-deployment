from fastapi import FastAPI

app = FastAPI(title="AI Starter Kit Backend")

@app.get("/health")
def health():
    return {
        "mesaj": "Bu endpoint github actions ile avtomatik yenilenib"
    }
