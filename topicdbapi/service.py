from fastapi import FastAPI


from .models.attribute_model import AttributeModel
from .models.language import Language

from .dependencies import get_store

store = get_store()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "TopicDB API Service"}


@app.get("/attributes/{map}/{attribute_id}")
async def get_attribute(map: int, attribute_id: str):
    attribute = await store.get_attribute(map, attribute_id)
    result = AttributeModel.from_orm(attribute)

    return result


@app.get("/entity-attributes/{map}/{entity_id}")
async def get_attributes(map: int, entity_id: str, scope: str = None, language: Language = None):
    result = []
    attributes = await store.get_attributes(map, entity_id, scope, language)

    for attribute in attributes:
        result.append(AttributeModel.from_orm(attribute))

    return result
