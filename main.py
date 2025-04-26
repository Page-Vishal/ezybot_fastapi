from fastapi import FastAPI
from pydantic import BaseModel
from Code.ezybot import response_from_bot

app = FastAPI()

class queryRequest(BaseModel):
    query: str

class messageResponse(BaseModel):
    response: str

@app.post("/chat", response_model=messageResponse)
async def response(question: queryRequest):
    try:
        response = await response_from_bot(question.query)
        return { "response" : response }
    except Exception as e:
        print("Error:", e)
        return {"response": "Oops, something went wrong."}