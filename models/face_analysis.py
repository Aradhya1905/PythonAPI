from pydantic import BaseModel

class FaceAnalysisResult(BaseModel):
    is_real: bool
    antispoof_score: float

class FaceAnalysisResponse(BaseModel):
    Result: FaceAnalysisResult
    Status: bool
    Message: str

class ExceptionApiResponse(BaseModel):
    Result: None
    Status: bool
    Message: str

class ApiResponse(BaseModel):
    Result: object | None
    Status: bool
    Message: str