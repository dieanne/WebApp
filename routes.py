from flask import render_template, flash, redirect, request, url_for, send_from_directory
from app import app
from datetime import datetime as dt
from forms import UploadForm, LoginForm
from werkzeug.utils import secure_filename
from database import insert, retrieve
from db.models import Entry
import config
import os 

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
            title = 'Home')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    form = UploadForm(request.form)
    if request.method == 'POST':     #  and form.validate():
        name = form.name.data
        subject = form.subject.data
        homework = form.homework.data
        file = request.files['file'] 
        date = dt.now()
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            entry = Entry(name, subject, homework, filename, date)
            insert(entry)
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            return render_template('upload.html', 
            title = 'Upload',
            form = form)
    else:        
        return render_template('upload.html', 
        title = 'Upload',
        form = form)


@app.route('/admin', methods = ['GET', 'POST'])
def admin_login():
    form = LoginForm(request.form)    
    if request.method == 'POST': 
        if( form.user.data == 'admin' and form.password.data == config.ADMIN_PASSWORD ):
            return redirect(url_for('admin_index'))       
        else:
            return redirect(url_for('index'))
    else:
        return render_template('admin_login.html',
                title = 'Admin - Log in',
                form = form)
   

@app.route('/admin/index')
def admin_index():
    entries =  retrieve()
    return render_template('admin_index.html',
                title = 'Admin - Stuff',
                entries = entries)