import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ForensIQ Vision API"}

import numpy as np
from PIL import Image

def test_detect_ai_image_placeholder():
    # Create a dummy image file
    image = Image.fromarray(np.uint8(np.random.rand(100, 100, 3) * 255))
    image.save("dummy_image.png")

    with open("dummy_image.png", "rb") as f:
        response = client.post("/detect_ai_image", files={"file": ("dummy_image.png", f, "image/png")})

    os.remove("dummy_image.png")

    assert response.status_code == 200
    json_response = response.json()
    assert json_response["is_ai_generated"] is True
    assert "confidence" in json_response
    assert "detected_artifacts" in json_response
    assert "heatmap" in json_response
    assert "explanation" in json_response
