from deepface import DeepFace
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "jasdjvnvdwn78"

UPLOAD_FOLDER = "static/uploads"
VERIFIED_FOLDER = 'static/verifieds'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['VERIFIED_FOLDER'] = VERIFIED_FOLDER

registered_faces = {}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/')
def upload_form():
    return render_template('register.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('Face has been registered.')
        
        registered_faces[filename] = {'first_name': first_name, 'last_name': last_name, 'file_path': file_path}
        
        return render_template('register.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

def recognize_face_image(target_image_path, registered_faces):
    recognized_name = "Unknown"
    for name, face_data in registered_faces.items():
        result = DeepFace.verify(
            target_image_path,
            face_data['file_path'],
            enforce_detection=False
        )
        if result["verified"]:
            recognized_name = f"{face_data['first_name']} {face_data['last_name']}"
            break
    return recognized_name

@app.route('/recognize', methods=["GET", "POST"])
def recognize_face():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No image uploaded"
        
        file = request.files['file']
        if file.filename == '':
            flash("No name for the image")
            return redirect(url_for('recognize_face'))
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['VERIFIED_FOLDER'], filename))
            
            recognized_name = recognize_face_image(
                os.path.join(app.config['UPLOAD_FOLDER'], filename),
                registered_faces
            )
            
            return render_template('recognize.html', recognized_name=recognized_name, filename=filename)

    return render_template('recognize.html')


if __name__ == "__main__":
    app.run()
