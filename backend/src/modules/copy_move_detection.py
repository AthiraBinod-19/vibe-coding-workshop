import cv2
import numpy as np

def detect_copy_move(image: np.ndarray):
    """
    Detects copy-move forgery in an image using a placeholder method.
    This is a simplified version and not a robust detection method.

    Args:
        image: The input image as a NumPy array.

    Returns:
        A tuple containing:
        - similarity_score (float): A score indicating the likelihood of copy-move forgery.
        - highlighted_image (np.ndarray): The image with duplicated regions highlighted.
    """
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use SIFT to detect keypoints and descriptors
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray_image, None)

    # Use a FLANN-based matcher to find potential matches
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(descriptors, descriptors, k=2)

    # Filter good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance and m.queryIdx != m.trainIdx:
            good_matches.append(m)

    similarity_score = len(good_matches) / len(keypoints) if len(keypoints) > 0 else 0

    # Highlight the matched regions (for simplicity, we draw lines between matched keypoints)
    highlighted_image = cv2.drawMatches(image, keypoints, image, keypoints,
                                        [m for m in good_matches], None,
                                        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return similarity_score, highlighted_image
