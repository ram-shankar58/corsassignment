from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON
with open("marks.json", "r") as f:
    students = json.load(f)

@app.get("/api")
def get_marks(name: list[str]):
    marks = []
    for n in name:
        student = next((s for s in students if s["name"] == n), None)
        marks.append(student["marks"] if student else None)  # None if name not found
    return {"marks": marks}
