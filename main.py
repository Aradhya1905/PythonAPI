from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import routes
from core.config import settings
import uvicorn

app = FastAPI(title="My Facial Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.allowed_origins,
    allow_methods = ["GET", "POST"],
    allow_headers = ["*"] 
)
    
app.include_router(routes.router, tags=["routes"])
app.include_router(routes.router, tags=["face analysis"])

@app.get("/")
async def root():
    return {"message": "Welcome face analysis API!"}

@app.get("/health")
async def health():
    return {"message": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)