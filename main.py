from fastapi import FastAPI
from pydantic import BaseModel
from setup_langchain import generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_llm(request: QueryRequest):
    response = generate_response(request.query)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
