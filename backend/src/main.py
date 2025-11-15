from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import cv2
import numpy as np
import base64
from modules.splicing_detection import detect_splicing
from modules.copy_move_detection import detect_copy_move
from modules.retouching_detection import detect_retouching
from modules.inpainting_detection import detect_inpainting
from modules.gan_detection import detect_gan
from modules.ai_image_detection import detect_ai_generated_image
from modules.ai_video_detection import detect_ai_generated_video
import tempfile
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the ForensIQ Vision API"}

async def read_image(file: UploadFile):
    """Reads and decodes the uploaded image file."""
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

@app.post("/detect_forgery")
async def detect_forgery(file: UploadFile = File(...)):
    """
    Detects whether an image has been manipulated using various forgery detection methods.
    """
    image = await read_image(file)

    splicing_prob, _ = detect_splicing(image)
    copy_move_score, _ = detect_copy_move(image.copy())
    retouching_prob, _ = detect_retouching(image)
    inpainting_prob, _ = detect_inpainting(image)
    gan_prob, _ = detect_gan(image)

    # Example thresholds
    splicing_threshold = 0.5
    copy_move_threshold = 0.1
    retouching_threshold = 0.6
    inpainting_threshold = 0.2
    gan_threshold = 0.5 # Example threshold for GAN

    manipulated = (splicing_prob > splicing_threshold or
                 copy_move_score > copy_move_threshold or
                 retouching_prob > retouching_threshold or
                 inpainting_prob > inpainting_threshold or
                 gan_prob > gan_threshold)
    confidence = max(splicing_prob, copy_move_score, retouching_prob, inpainting_prob, gan_prob)

    return {"manipulated": manipulated, "confidence": float(confidence)}

@app.post("/classify_forgery")
async def classify_forgery(file: UploadFile = File(...)):
    """
    Classifies the type of forgery in an image.
    """
    image = await read_image(file)
    splicing_prob, _ = detect_splicing(image)
    copy_move_score, _ = detect_copy_move(image.copy())
    retouching_prob, _ = detect_retouching(image)
    inpainting_prob, _ = detect_inpainting(image)
    gan_prob, _ = detect_gan(image)

    # Determine the most likely forgery type based on the highest score
    scores = {
        "splicing": splicing_prob,
        "copy-move": copy_move_score,
        "retouching": retouching_prob,
        "inpainting": inpainting_prob,
        "gan": gan_prob
    }

    # Get the forgery type with the highest score
    max_score_type = max(scores, key=scores.get)
    max_score = scores[max_score_type]

    # Set a minimum threshold for detection
    if max_score > 0.5: # General threshold
        forgery_type = max_score_type
        confidence = max_score
    else:
        forgery_type = "none"
        confidence = 1 - max_score

    return {"forgery_type": forgery_type, "confidence": float(confidence)}

@app.post("/generate_heatmap")
async def generate_heatmap(file: UploadFile = File(...)):
    """
    Generates a heatmap for splicing detection.
    """
    image = await read_image(file)
    _, heatmap = detect_splicing(image)

    # Encode the heatmap as a Base64 string
    _, buffer = cv2.imencode('.png', heatmap)
    heatmap_base64 = base64.b64encode(buffer).decode('utf-8')

    return {"heatmap_image": heatmap_base64}

@app.post("/generate_copy_move_visualization")
async def generate_copy_move_visualization(file: UploadFile = File(...)):
    """
    Generates a visualization of copy-move forgery detection.
    """
    image = await read_image(file)
    _, highlighted_image = detect_copy_move(image)

    # Encode the highlighted image as a Base64 string
    _, buffer = cv2.imencode('.png', highlighted_image)
    visualization_base64 = base64.b64encode(buffer).decode('utf-8')

    return {"visualization_image": visualization_base64}

@app.post("/detect_ai_video")
async def detect_ai_video(file: UploadFile = File(...)):
    """
    Detects whether a video is AI-generated.
    """
    try:
        # Save the uploaded video to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
            tmp.write(await file.read())
            video_path = tmp.name

        # Process the video
        result = detect_ai_generated_video(video_path)

    finally:
        # Clean up the temporary file
        if 'video_path' in locals() and os.path.exists(video_path):
            os.unlink(video_path)

    return result

@app.post("/detect_ai_image")
async def detect_ai_image(file: UploadFile = File(...)):
    """
    Detects whether an image is AI-generated.
    """
    image = await read_image(file)
    result = detect_ai_generated_image(image)
    return result

@app.post("/generate_gan_visualization")
async def generate_gan_visualization(file: UploadFile = File(...)):
    """
    Generates a visualization of GAN detection (tampering map).
    """
    image = await read_image(file)
    _, tampering_map = detect_gan(image)

    # Encode the tampering map as a Base64 string
    _, buffer = cv2.imencode('.png', tampering_map)
    visualization_base64 = base64.b64encode(buffer).decode('utf-8')

    return {"visualization_image": visualization_base64}

@app.post("/generate_inpainting_visualization")
async def generate_inpainting_visualization(file: UploadFile = File(...)):
    """
    Generates a visualization of inpainting detection (mask).
    """
    image = await read_image(file)
    _, mask = detect_inpainting(image)

    # Encode the mask as a Base64 string
    _, buffer = cv2.imencode('.png', mask)
    visualization_base64 = base64.b64encode(buffer).decode('utf-8')

    return {"visualization_image": visualization_base64}

@app.post("/generate_retouching_visualization")
async def generate_retouching_visualization(file: UploadFile = File(...)):
    """
    Generates a visualization of retouching detection (noise map).
    """
    image = await read_image(file)
    _, noise_map = detect_retouching(image)

    # Encode the noise map as a Base64 string
    _, buffer = cv2.imencode('.png', noise_map)
    visualization_base64 = base64.b64encode(buffer).decode('utf-8')

    return {"visualization_image": visualization_base64}
