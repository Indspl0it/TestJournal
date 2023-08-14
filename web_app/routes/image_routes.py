```python
from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from web_app.models.Image import Image
from web_app.services.image_service import save_image, get_image

image_routes = Blueprint('image_routes', __name__)

@image_routes.route('/image/upload', methods=['POST'])
@login_required
def upload_image():
    if 'file' not in request.files:
        flash('No file part', 'image_message')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'image_message')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = save_image(file)
        new_image = Image(filename=filename, user_id=current_user.id)
        db.session.add(new_image)
        db.session.commit()
        flash('Image successfully uploaded and displayed', 'image_message')
        return redirect(url_for('dashboard'))

@image_routes.route('/image/<filename>')
@login_required
def display_image(filename):
    return redirect(url_for('static', filename='images/' + filename))

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```