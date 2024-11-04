from fastapi import APIRouter, Depends, HTTPException
from typing import List, Type
from peewee import Model
from app.auth.injections import is_admin
from app.core.database import db

from app.serializers.enumeration import EnumerationCreate, EnumerationUpdate, EnumerationResponse


def create_crud_router(model: Type[Model]):
    router = APIRouter()

    @router.get("/", response_model=List[EnumerationResponse])
    async def get_all():
        return list(model.select())

    @router.post("/", response_model=EnumerationResponse)
    async def create(item: EnumerationCreate, current_user: dict = Depends(is_admin)):
        with db.atomic():
            db_item = model.create(**item.dict())
        return db_item

    @router.get("/{item_id}", response_model=EnumerationResponse)
    async def get_one(item_id: str, current_user: dict = Depends(is_admin)):
        item = model.get_or_none(model.id == item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.put("/{item_id}", response_model=EnumerationResponse)
    async def update(item_id: str, item: EnumerationUpdate, current_user: dict = Depends(is_admin)):
        db_item = model.get_or_none(model.id == item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        db_item.id = item.id
        db_item.save()
        return db_item

    @router.delete("/{item_id}", response_model=EnumerationResponse)
    async def delete(item_id: str, current_user: dict = Depends(is_admin)):
        db_item = model.get_or_none(model.id == item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        db_item.delete_instance()
        return db_item

    return router