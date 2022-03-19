from flask import redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField ,FileField, SubmitField
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired


class AddPropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    numberofbed = StringField('Number Of Bedroom(s)', validators=[InputRequired()])
    numberofbath = StringField('Number Of Bathroom(s)', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    residence_type = SelectField(u'Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = StringField('Description', widget=TextArea())
    image = FileField('Property Image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField()
    