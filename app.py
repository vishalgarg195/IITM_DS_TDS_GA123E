from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    data = {"email": "23ds2000079@ds.study.iitm.ac.in", "message": "Hello from Codespaces!"}
    return JSONResponse(content=data)

