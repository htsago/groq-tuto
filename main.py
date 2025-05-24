from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from controller import call_groq
from models import Question

load_dotenv()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/api/v1/process_query")
def process_query(input: Question):

    return call_groq(input)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)
