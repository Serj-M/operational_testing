import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.api_base.question import handler_question


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['*']
)

@app.get("/")
def read_root():
    return "Hello!"


class HumanMessage(BaseModel):
    human_message: str = Field(..., description="Текст вопроса")

@app.post("/question")
async def question(params: HumanMessage) -> dict:
    human_message = params.human_message
    response: str = await handler_question(human_message)
    result = {
        "question": human_message,
        "answer": response
    }
    return result


# uvicorn backend.api_base.main:app --reload
if __name__ == "__main__":
    uvicorn.run("backend.api_base.main:app", host="127.0.0.1", port=8000, reload=True)
