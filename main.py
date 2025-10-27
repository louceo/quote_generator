from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles 
from quote_gen import get_quote


app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')


@app.get("/")
def home():
    return FileResponse('static/index.html')

@app.get("/quote")
def quote():
    quote_data = get_quote()
    return JSONResponse(quote_data)
