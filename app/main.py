from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import shutil, os

from app.esg_rag_engine import analyze_document_with_esg_guidelines

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analisar", response_class=HTMLResponse)
async def analisar(request: Request, arquivo: UploadFile, pergunta: str = Form(...)):
    caminho = os.path.join(UPLOAD_DIR, arquivo.filename)
    with open(caminho, "wb") as f:
        shutil.copyfileobj(arquivo.file, f)

    resultado = analyze_document_with_esg_guidelines(caminho, pergunta)

    return templates.TemplateResponse("resultado.html", {
        "request": request,
        "pergunta": resultado["pergunta"],
        "resposta": resultado["resposta"]
    })
