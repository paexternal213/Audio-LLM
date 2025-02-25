#Libraries
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#Object Initialization
app = FastAPI()

templates = Jinja2Templates(directory="templates")
#Rendering 'index.html' template
@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
     return templates.TemplateResponse("index.html",{"request": request})
