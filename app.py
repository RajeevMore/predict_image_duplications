#from typing import Annotated
import uvicorn
from code import finddedup
import os
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/document-dedup")
async def create_upload_file(file: UploadFile):

    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    tuple1 = finddedup()
    Not_duplicate, Duplicate=tuple1[0],tuple1[1]
    if file.filename in Not_duplicate:
        return { "isDocDuplicate": False }
    elif file.filename in Duplicate:
        folder_path = "uploaded_files/"
        file_name = file.filename  

        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        return{"isDocDuplicate": True }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10000)
