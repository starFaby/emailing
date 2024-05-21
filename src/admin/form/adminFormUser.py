from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, length
class AdminFormUserWtf(FlaskForm):
    id = StringField('id')
    nombres = StringField('nombres', validators=[InputRequired('El nombres es requerido'), length(min=5, max=20, message='Minimo 5 caracteres y maximo 20 caracteres')])
    apellidos = StringField('apellidos', validators=[InputRequired('El apellidos es requerido'), length(min=5, max=20, message='Minimo 5 caracteres y maximo 20 caracteres')])
    email = StringField('email', validators=[InputRequired('El email es requerido'), length(min=5, max=50, message='Minimo 5 caracteres y maximo 50 caracteres')])
    direccion = StringField('direccion', validators=[InputRequired('La direccion es requerido'), length(min=5, max=20, message='Minimo 5 caracteres y maximo 20 caracteres')])
    celular = StringField('celular', validators=[InputRequired('El celular es requerido'), length(min=5, max=20, message='Minimo 5 caracteres y maximo 20 caracteres')])
    estado = SelectField('estado', choices=[('1','Activo'), ('0','Inactivo')])