# ForensIQ Vision Backend

This is the backend for the ForensIQ Vision application. It provides a FastAPI-based API for detecting various types of image and video manipulation.

## Datasets

The models used in this application are trained on a variety of datasets. Here are some of the key datasets used for training forgery detection models:

### Deepfake Detection

*   **FaceForensics++**: [https://github.com/ondyari/FaceForensics](https://github.com/ondyari/FaceForensics)
*   **DFDC (Deepfake Detection Challenge)**: [https://www.kaggle.com/c/deepfake-detection-challenge](https://www.kaggle.com/c/deepfake-detection-challenge)
*   **Celeb-DF v2**: [https://github.com/yuezunli/celeb-deepfakeforensics](https://github.com/yuezunli/celeb-deepfakeforensics)

### AI-Generated Image Detection

*   **Stable Diffusion**: [https://huggingface.co/datasets/laion/laion-stable-diffusion-2-1](https://huggingface.co/datasets/laion/laion-stable-diffusion-2-1)
*   **Midjourney**: Datasets are not publicly available, but models can be trained on scraped images.
*   **LAION**: [https://laion.ai/blog/laion-5b/](https://laion.ai/blog/laion-5b/)
*   **GAN-generated Datasets**:
    *   **StyleGAN2**: [https://github.com/NVlabs/stylegan2](https://github.com/NVlabs/stylegan2)
    *   **BigGAN**: [https://tfhub.dev/deepmind/biggan-256/2](https://tfhub.dev/deepmind/biggan-256/2)
