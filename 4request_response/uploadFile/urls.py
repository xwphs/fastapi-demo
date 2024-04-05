from fastapi import APIRouter, UploadFile
import os.path
import shutil
from typing import List
router = APIRouter()

@router.post('/uploadFiles')
async def upload_file(files: List[UploadFile]):
    for file in files:
        dest_path = os.path.join('img', file.filename)
        with open(dest_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    return {"message": "File uploaded successfully!"}
