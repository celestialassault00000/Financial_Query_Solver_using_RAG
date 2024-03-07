from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

from src.chat import main

def main2():
    responses = []
    for _ in range(5):
        user_input = input("User: ")
        # Process the user input (you can replace this with your actual chatbot logic)
        response = f"Chatbot: Processing {user_input}"
        responses.append(response)
    return responses

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def chat_endpoint(request: Request, user_input: str = Form(...)):
    responses = main2()
    return templates.TemplateResponse("index.html", {"request": request, "user_input": user_input, "responses": responses})

