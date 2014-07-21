from wtforms import Form
from wtforms import TextField, BooleanField, SelectField, FileField, PasswordField, validators


class UploadForm(Form):
    name = TextField('Name', [validators.Required()])
    subject = SelectField('Subject', choices=[('ai', 'Artificial Inteligence'), ('oop', 'Object Oriented Programming'), ('o', 'Other')])
    homework = SelectField('Homework', choices=[(i,'Homework'+str(i)) for i in range(1,11)])
    file = FileField('File')
 
class LoginForm(Form):
     user = TextField('User', [validators.Required()])
     password = PasswordField('Pass', [validators.Required()])