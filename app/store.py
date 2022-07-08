from fastapi import FastAPI, Path, Response
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# A BaseModel class to enforce the structure of
# the  incoming POST request and verify that
class Post(BaseModel):
    key: str
    value: str


store = {"abc-1":"abc-1","abc-2":"abc-2","xyz-1":"xyz-1","xyz-2":"xyz-2"}

@app.get("/get/{key}")
def get(key: str = Path(None, description = "key for value needed in get response")):
    if key in store:
        return store[key]
    else:
        return

@app.post("/set")
def set(payload: Post, response: Response) -> None:
    store[payload.key] = payload.value
    print(store)

@app.get("/search")
def search(*,prefix: Optional[str] = None,suffix: Optional[str] = None):
    response = []
    if prefix:
        for k in store:
            if k.startswith(prefix):
                response.append(store[k])
            else:
                pass
    if suffix:
        for k in store:
            if k.endswith(suffix):
                response.append(store[k])
            else:
                pass
    return response



if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
