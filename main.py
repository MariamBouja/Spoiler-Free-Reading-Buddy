from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(request: dict):
    return {"answer": "You asked " + request["question"], "chapter": request["chapter"]} 