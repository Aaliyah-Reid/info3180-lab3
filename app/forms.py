from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Email
from flask_wtf.csrf import CSRFProtect


class ContactForm(FlaskForm):
    username = StringField('Name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired(), Email()])    
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
