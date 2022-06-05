from fastapi import APIRouter, HTTPException

from ..models.attribute_model import AttributeModel
from ..models.language import Language

from ..dependencies import get_store

store = get_store()

router = APIRouter(prefix="/maps/{map}/attributes", tags=["attributes"], responses={404: {"description": "Not found"}})


@router.get("/{attribute_id}")
async def get_attribute(map: int, attribute_id: str):
    attribute = await store.get_attribute(map, attribute_id)
    if not attribute:
        raise HTTPException(status_code=404, detail="Attribute not found")
    result = AttributeModel.from_orm(attribute)

    return result


@router.get("/{entity_id}/entities")
async def get_attributes(map: int, entity_id: str, scope: str = None, language: Language = None):
    result = []
    attributes = await store.get_attributes(map, entity_id, scope, language)
    if not attributes:
        raise HTTPException(status_code=404, detail="Attributes not found")

    for attribute in attributes:
        result.append(AttributeModel.from_orm(attribute))

    return result
