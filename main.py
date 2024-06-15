from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI OCR Application"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    text = pytesseract.image_to_string(image)
    return JSONResponse(content={"text": text})
