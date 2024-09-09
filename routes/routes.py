# Add routes here

from fastapi import APIRouter, Request
from api.endpoints import face_analysis

router = APIRouter(prefix="/api")

@router.get("/")
async def root():
    return {"message": "Welcome to my face analysis API!"}

# Face Analysis Routes
@router.post("/face/checkImageForSpoof")
async def check_image_for_spoof(request: Request):
    return await face_analysis.analyze_image(request)