# Import the Images module from pillow
from PIL import Image

def improve_image(image_id):
    # Open the image by specifying the image path.
    image_path = f"application/static/images/{image_id}"
    image_file = Image.open(image_path)

    # increase
    image_file.save(image_id, quality=95)

    return True
