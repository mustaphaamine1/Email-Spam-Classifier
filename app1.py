from fastapi import FastAPI, Form, HTTPException, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils import model_predict

app = FastAPI()
templates = Jinja2Templates(directory="templates") 

@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/predict")
async def predict(request: Request,content: str = Form(...)):
    prediction = model_predict(content) 

    return templates.TemplateResponse("index.html", {"request": request,"prediction": prediction, "email": content})

if __name__ == "__main__":
    uvicorn.run("app1:app", host="0.0.0.0", port=8080, reload=True)