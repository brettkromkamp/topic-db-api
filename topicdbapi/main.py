from fastapi import FastAPI


from .dependencies import get_store
from .routers import attributes

app = FastAPI()


app.include_router(attributes.router)


@app.get("/")
async def root():
    return {"message": "TopicDB API Service"}
