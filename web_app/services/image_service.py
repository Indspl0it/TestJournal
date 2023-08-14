from flask import current_app
from PIL import Image
import os

from web_app.models.Image import ImageModel

def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(current_app.root_path, 'static/images', image_fn)

    output_size = (125, 125)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(image_path)

    return image_fn

def get_image(image_id):
    image = ImageModel.query.get(image_id)
    if image:
        return image
    else:
        return None

def delete_image(image_id):
    image = ImageModel.query.get(image_id)
    if image:
        db.session.delete(image)
        db.session.commit()
        return True
    else:
        return False

def update_image(image_id, form_image):
    image = ImageModel.query.get(image_id)
    if image:
        image.image_file = save_image(form_image)
        db.session.commit()
        return True
    else:
        return False