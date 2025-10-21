from fastapi import FastAPI
from src.data.ingest import download_monthly_data
from pydantic import BaseModel

class DataInput(BaseModel):
    month: int
    year: int

app = FastAPI()

@app.get("/ping")
def health_check():
    return {"status_code": 200}

@app.post("/download")
def downlod_data(input:DataInput):
        
    file_path=download_monthly_data(input.year, input.month)
    if file_path:
        return {"status_code":200, "file_path": str(file_path)}
    else:
        return {"status_code":500, "message":"Download failed"}
        
        

