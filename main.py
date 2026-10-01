from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    chapter: int

class QueryResponse(BaseModel):
    answer: str
    chapter: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(request: QueryRequest) -> QueryResponse:
    return QueryResponse(answer="You asked " + request.question, chapter=request.chapter)

