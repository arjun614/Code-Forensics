from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_code
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI Forensics API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeInput(BaseModel):
    code: str


@app.get("/")
def home():
    return {
        "message": "AI Forensics API is running"
    }


@app.post("/analyze")
def analyze(input_data: CodeInput):

    result, confidence, probabilities, forensic_analysis = predict_code(
        input_data.code
    )

    return {
        "prediction": result,
        "confidence": round(confidence, 2),
        "probabilities": probabilities,
        "forensic_analysis": forensic_analysis
    }