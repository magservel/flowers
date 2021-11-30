from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    x = StringField('X', validators=[DataRequired()])
    y = StringField('Y', validators=[DataRequired()])
    submit = SubmitField('Add data pair')


class InferForm(FlaskForm):
    x = StringField('X', validators=[DataRequired()])
    submit = SubmitField('Infer data')
