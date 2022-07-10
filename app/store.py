from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import uvicorn

from prometheusMetric import PrometheusMiddleware

store = {"abc-1":"abc-1","abc-2":"abc-2","xyz-1":"xyz-1","xyz-2":"xyz-2"}

app = FastAPI()


app.add_middleware(PrometheusMiddleware)


@app.get("/metrics")
def metrics():
    res=generate_latest(HTTP_LATENCY_STATUS_KEYS).decode('ascii')+generate_latest(HTTP_RESPONSE).decode('ascii')
    return Response(res)





# A BaseModel class to enforce the structure of
# the  incoming POST request and verify that
class Post(BaseModel):
    key: str
    value: str




@app.get("/get/{key}")
def get(key: str = Path(None, description = "key for value needed in get response")):
    time.sleep(5)
    if key in store:
        return store[key]
    else:
        return

@app.post("/set")
def set(payload: Post) -> None:
    store[payload.key] = payload.value


@app.get("/search")
def search(*,prefix: Optional[str] = None,suffix: Optional[str] = None):
    res = []
    if prefix:
        for k in store:
            if k.startswith(prefix):
                res.append(store[k])
            else:
                pass
    if suffix:
        for k in store:
            if k.endswith(suffix):
                res.append(store[k])
            else:
                pass
    return res



if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
