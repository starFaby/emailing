from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField, FloatField
from wtforms.validators import InputRequired, length
class ClientFormProductowtf(FlaskForm):
    id = StringField('id')
    nombre = StringField('nombre', validators=[InputRequired('El nombre es requerido'), length(min=5, max=20, message='Minimo 5 caracteres y maximo 20 caracteres')])
    image = StringField('image', validators=[InputRequired('La imagen es requerido'), length(min=5, max=300, message='Minimo 5 caracteres y maximo 300 caracteres')])
    detalle = StringField('detalle', validators=[InputRequired('El detalle es requerido'), length(min=5, max=100, message='Minimo 5 caracteres y maximo 100 caracteres')])
    precio = FloatField('precio', validators=[InputRequired('El precio es requerido')])
    stock = IntegerField('stock', validators=[InputRequired('El stock es requerido')])
    estado = SelectField('estado', choices=[('1','Activo'), ('0','Inactivo')])