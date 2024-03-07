from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse




from src.load_Cohere import co 
from src.retriever import retriever
def query_builder(retieved_Context, user_query):
    input_json = {"user_query": user_query, "context": retieved_Context}
    s=""" Attached below is the json format which consists of user_query and conext of the user_query which contain some retrieved information from literature regarding user_query, based on that context you will answer the user query. input json is {}""".format(input_json)
    return s
from src.load_Cohere import co 
from src.retriever import retriever
def query_builder(retieved_Context, user_query):
    input_json = {"user_query": user_query, "context": retieved_Context}
    s=""" Attached below is the json format which consists of user_query and conext of the user_query which contain some retrieved information from literature regarding user_query, based on that context you will answer the user query. input json is {}""".format(input_json)
    return s



def main(input_query):
    input_query= query_builder(retriever(input_query), input_query)
    response = co.chat(message=input_query)
    return response.text


if __name__ == "__main__":
    main()

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
 # Import your function

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": ""})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, query: str = Form(...)):
    input_query = query  # Assuming retriever is defined elsewhere
    response_text = main(input_query)  # Call your function with the processed input

    return templates.TemplateResponse("index.html", {"request": request, "chat_history": response_text})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
