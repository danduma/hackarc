from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Mock data (replace with your actual data source)
class MouseData(BaseModel):
    id: int
    name: str
    age: int
    weight: float
    strain: str

mice_data = [
    MouseData(id=1, name="Mickey", age=2, weight=20.5, strain="C57BL/6"),
    MouseData(id=2, name="Minnie", age=1, weight=18.3, strain="BALB/c"),
    # Add more mock data as needed
]

mouse_images = {
    1: "/static/images/mouse1.jpg",
    2: "/static/images/mouse2.jpg",
    # Add more image paths as needed
}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/mice")
async def mice(request: Request):
    return templates.TemplateResponse("mice.html", {"request": request, "mice": mice_data})

@app.get("/query")
async def query(request: Request):
    return templates.TemplateResponse("query.html", {"request": request})

@app.get("/api/mice")
async def get_mice():
    return mice_data

@app.get("/api/mouse/{mouse_id}")
async def get_mouse(mouse_id: int):
    mouse = next((m for m in mice_data if m.id == mouse_id), None)
    if mouse:
        return {**mouse.dict(), "image": mouse_images.get(mouse_id)}
    return {"error": "Mouse not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
