
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static/css"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", 
    )


@app.get("/primeraEtapa", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request, name="primeraEtapa.html",
    )


@app.get("/segundaEtapa", response_class=HTMLResponse)
async def contacto(request: Request):
    return templates.TemplateResponse(
        request=request, name="segundaEtapa.html", 
    )

@app.get("/terceraEtapa", response_class=HTMLResponse)
async def SegundaEtapa(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="terceraEtapa.html",
    )