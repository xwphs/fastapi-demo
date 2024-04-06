from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
import subprocess
import os.path

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)  ## 禁用docs
class Parameter(BaseModel):
    para: str = ''

@app.post('/scripts/{script_path:path}',tags=['Calling scripts'] ,description='远程执行shell脚本')
async def scripts(script_path: str, para: Optional[Parameter] = None):
    base_path='/opt/scripts'        ########## 这是脚本的根目录文件，需要根据情况修改  ########
    script_path = os.path.join(base_path, script_path)
    if para is None:
        result = subprocess.run(args=('sh', script_path), capture_output=True, text=True)
    else:
        result = subprocess.run(args=('sh', script_path, para.para), capture_output=True, text=True)
    print(result.stdout)
    return {"stdout": result.stdout, 
            "stderr": result.stderr}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8089, reload=True)