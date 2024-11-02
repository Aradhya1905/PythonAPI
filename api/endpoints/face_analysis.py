from fastapi import APIRouter, Request, HTTPException
from deepface import DeepFace
from models.face_analysis import FaceAnalysisResult, ApiResponse, ExceptionApiResponse

router = APIRouter()

@router.post("/checkImageForSpoof")
async def handle_image_analysis(request: Request):
    return await analyze_image(request)

async def analyze_image(request: Request):
    body = await request.json()
    image_fromRequestBody = body.get("image")
    string_toContenate = "data:image/jpg;base64,"
    base64_image = string_toContenate + image_fromRequestBody
    if not base64_image:
        raise HTTPException(status_code=400, detail="No image provided")
    
    if not isinstance(base64_image, str):
        raise HTTPException(status_code=400, detail="Image must be a base64 encoded string")

    try:    
        # Check if Photo is face or object
        # try:    
        #     result1  = DeepFace.analyze(img_path=base64_image,detector_backend="retinaface",align=True, enforce_detection=True, anti_spoofing=True)
        #     print(result1, "result1")
        # except Exception as e:
        #     print(f"Error: {str(e)}")
        #     return ApiResponse(
        #         Result=None,
        #         Status=False,
        #         Message=f"Error processing image: {str(e)} Please try again..."
        #     )
        result = DeepFace.extract_faces(img_path=base64_image,detector_backend="retinaface",align=True,normalize_face=True, enforce_detection=True, anti_spoofing=True)
       
        if(len(result) == 0):
            return ApiResponse(
                Result=result,
                Status=False,
                Message="Something went wrong. No faces detected! Please try again..."
            )
        if(len(result) > 1):
            print("len 2",result)
            return ApiResponse(
                Result=None,
                Status=False,
                Message="Multiple faces detected, the image should contain only one face!! Please check and try again..."
            )
        
        if len(result) == 1:
            face_analysis_result = FaceAnalysisResult(
                is_real=result[0].get('is_real'),
                antispoof_score=result[0].get('antispoof_score') * 100
            )
            return ApiResponse(
                Result=face_analysis_result,
                Status=True,
                Message="Success"
            )
    except Exception as e:
        print(f"Error: {str(e)}")
        if "face could not be detected" in str(e).lower():
            return ApiResponse(
                Result=None,
                Status=False,
                Message="Unable to detect a face in your image. Please ensure your face is clearly visible and try again."
            )
        return ExceptionApiResponse(
            Result=None,
            Status=False,
            Message=f"Error processing image: {str(e)} Please try again..."
        )