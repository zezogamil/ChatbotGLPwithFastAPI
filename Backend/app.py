
# from engineio.static_files import content_types
from fastapi import FastAPI, UploadFile, File, Form, HTTPException

# from fastapi import UploadFile, File

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello GLP Software. all works just good"}


@app.post("/load")
async def load_file(file: UploadFile = File(...), extra_data: str = Form(None),):
    if file is None:
        raise HTTPException(status_code=400, detail="No file provided")
    print("Received file:", file.filename)
    if  file.filename.endswith((".pdf", ".csv", ".docx")):
        content_type = file.content_type
        file_bytes = await file.read()
        size = len(file_bytes)
    if not file.filename.endswith((".docx", ".pdf", ".csv")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    # file.filename.endswith("pdf" "csv" "docx")
    return {
        "filename": file.filename,
        "content_type": content_type,
        "size": size,
        "extra_data": extra_data
    }
    