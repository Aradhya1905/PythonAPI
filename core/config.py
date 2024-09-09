from pydantic import BaseModel
from typing import List

class Settings(BaseModel):
    app_name: str = "Face Analysis API"
    debug: bool = False
    allowed_origins: List[str] = ["*"]
    PORT: int = 9000

settings = Settings()