from fastapi import FastAPI
from pydantic import BaseModel
from plumber_agent import agent
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PincodeRequest(BaseModel):
    pincode: str

@app.post("/get-plumbers")
def get_plumbers(req: PincodeRequest):
    result = agent(req.pincode)
    return {"result": result}