from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Sistema de Pedidos em Tempo Real")

templates = Jinja2Templates(directory="templates")


# --- Endpoint para a Página Web ---
@app.get("/", response_class=HTMLResponse)
async def ler_pagina_pedidos(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# --- Endpoint da API para receber novos pedidos ---
@app.post("/pedidos")
async def criar_pedido():
    pass

