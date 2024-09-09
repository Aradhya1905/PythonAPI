from fastapi import APIRouter, HTTPException
from models.item import Item

router = APIRouter()

items = []

@router.post("/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@router.get("/", response_model=list[Item])
async def read_items():
    return items

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]