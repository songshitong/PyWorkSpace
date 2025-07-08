
https://fastapi.tiangolo.com/zh/tutorial/path-params/

安装
```
pip install fastapi
pip install "uvicorn[standard]"  #ASGI 服务器
```

ASGI（Asynchronous Server Gateway Interface）是一个用于连接Web服务器和应用程序框架的标准接口规范，旨在实现异步处理请求和响应。
它是对传统WSGI（Web Server Gateway Interface）的扩展，提供了更高的性能和可扩展性



路径参数
```
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5), # 校验>0,<10.5
    user_agent: Annotated[str | None, Header()] = None # 声明Header
    response_model=UserOut #声明返回的类型
    status_code=201, # 返回码  status.HTTP_201_CREATED
    tags=["items"] #文档的分组标签
    ):
    raise HTTPException(status_code=404, detail="Item not found") #抛出异常
    return UserOut 
```

查询参数   /items/{item_id}?item_id=xx&...   skip存在默认，limit可不传
```
from typing import Union
from fastapi import FastAPI, Query

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None,
    q: Union[str, None] = Query(default=None, max_length=50,pattern="^fixedquery$")  # 长度校验和正则校验
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
```

请求体
```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
    
 json:
 {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}   
```

表单类型
```
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
    
    
class FormData(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data    
```

文件上传
```
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```


中间件
```
import time

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```