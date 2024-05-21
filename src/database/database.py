from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------------------------
#----------usuario----------
#--------------------------
class Admin(db.Model):
    __tablename__='pfsadmin'

    pfsadminid = db.Column(db.Integer, primary_key=True)
    pfsadmincedula = db.Column(db.String(80), nullable=False)
    pfsadminnombres = db.Column(db.String(80), nullable=False)
    pfsadminapellidos = db.Column(db.String(80), nullable=False)
    pfsadminusername = db.Column(db.String(30), unique=True, nullable=False)
    pfsadminemail = db.Column(db.String(120), nullable=False)
    pfsadminpassword = db.Column(db.String(250), nullable=True)
    pfsadmindireccion = db.Column(db.String(100), nullable=True)
    pfsadmincellphone = db.Column(db.String(25), nullable=False)
    pfsadminphone = db.Column(db.String(20), nullable=False)
    pfsadminisadmin = db.Column(db.Boolean, default=False)
    pfsadminavatar = db.Column(db.String(250), nullable=True)
    pfsadminestado = db.Column(db.String(1), nullable=True)
    pfsadmincreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsadminpassword):
        self.pfsadminpassword = generate_password_hash(pfsadminpassword)

    def onGetCheckPassword(self, pfsadminpassword):
        return check_password_hash(self.pfsadminpassword, pfsadminpassword)

    def __init__(self, pfsadmincedula, pfsadminnombres, pfsadminapellidos, pfsadminusername, pfsadminemail, pfsadminpassword, pfsadmindireccion,  pfsadmincellphone, pfsadminphone, pfsadminisadmin, pfsadminavatar, pfsadminestado, pfsadmincreatedat):
        self.pfsadmincedula = pfsadmincedula
        self.pfsadminnombres = pfsadminnombres
        self.pfsadminapellidos = pfsadminapellidos
        self.pfsadminusername = pfsadminusername
        self.pfsadminemail = pfsadminemail
        self.pfsadminpassword = pfsadminpassword 
        self.pfsadmindireccion = pfsadmindireccion 
        self.pfsadmincellphone = pfsadmincellphone
        self.pfsadminphone = pfsadminphone
        self.pfsadminisadmin = pfsadminisadmin
        self.pfsadminavatar = pfsadminavatar
        self.pfsadminestado = pfsadminestado
        self.pfsadmincreatedat = pfsadmincreatedat

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('pfsadminid', 'pfsadmincedula', 'pfsadminnombres', 'pfsadminapellidos', 'pfsadminusername', 'pfsadminemail', 'pfsadminpassword', 'pfsadmindireccion',  'pfsadmincellphone', 'pfsadminphone', 'pfsadminisadmin', 'pfsadminavatar','pfsadminestado', 'pfsadmincreatedat')

adminSchema = AdminSchema()
adminSchema = AdminSchema(many=True)

#----------------------------
#----------PRODUCTO----------
#--------------------------
class Producto(db.Model):
    __tablename__='pfsemproductos'

    pfsemprodid = db.Column(db.Integer, primary_key=True)
    pfsemprodnombre = db.Column(db.String(80), nullable=False)
    pfsemprodimage = db.Column(db.String(300), nullable=False)
    pfsemproddetalle = db.Column(db.String(300), nullable=False)
    pfsemprodprecio = db.Column(db.Float, nullable=False) #float
    pfsemprodstock = db.Column(db.String(10), nullable=False) #int
    pfsemprodestado = db.Column(db.String(1), nullable=True)
    pfsemprodcreatedat = db.Column(db.String(11), nullable=True) 
    
    pfsemadminid = db.Column(db.Integer, db.ForeignKey('pfsadmin.pfsadminid',ondelete='CASCADE'), nullable=False)
    pfsemadmin = db.relationship('Admin',backref=db.backref('pfsemproductos',lazy=True))


    def __init__(self, pfsemprodnombre, pfsemprodimage, pfsemproddetalle, pfsemprodprecio, pfsemprodstock, pfsemprodestado, pfsemprodcreatedat, pfsemadminid):
        self.pfsemprodnombre = pfsemprodnombre
        self.pfsemprodimage = pfsemprodimage
        self.pfsemproddetalle = pfsemproddetalle
        self.pfsemprodprecio = pfsemprodprecio
        self.pfsemprodstock = pfsemprodstock
        self.pfsemprodestado = pfsemprodestado
        self.pfsemprodcreatedat = pfsemprodcreatedat
        self.pfsemadminid = pfsemadminid
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('pfsemprodid','pfsemprodnombre', 'pfsemprodimage', 'pfsemproddetalle', 'pfsemprodprecio', 'pfsemprodstock', 'pfsemprodestado', 'pfsemprodcreatedat','pfsemadminid')

productoSchema = ProductoSchema()
productoSchema = ProductoSchema(many=True)


#----------------------------
#----------User----------
#--------------------------
class User(db.Model):
    __tablename__='pfsemuser'

    pfsemuserid = db.Column(db.Integer, primary_key=True)
    pfsemusernombres = db.Column(db.String(80), nullable=False)
    pfsemuserapellidos = db.Column(db.String(300), nullable=False)
    pfsemuseremail = db.Column(db.String(300), nullable=False)
    pfsemuserdireccion = db.Column(db.String(300), nullable=False) #float
    pfsemusercelular = db.Column(db.String(10), nullable=False) #int
    pfsemuserestado = db.Column(db.String(1), nullable=True)
    pfsemusercreatedat = db.Column(db.String(11), nullable=True) 
    
    pfsemadminid = db.Column(db.Integer, db.ForeignKey('pfsadmin.pfsadminid',ondelete='CASCADE'), nullable=False)
    pfsemadmin = db.relationship('Admin',backref=db.backref('pfsemuser',lazy=True))


    def __init__(self, pfsemusernombres, pfsemuserapellidos, pfsemuseremail, pfsemuserdireccion, pfsemusercelular, pfsemuserestado, pfsemusercreatedat, pfsemadminid):
        self.pfsemusernombres = pfsemusernombres
        self.pfsemuserapellidos = pfsemuserapellidos
        self.pfsemuseremail = pfsemuseremail
        self.pfsemuserdireccion = pfsemuserdireccion
        self.pfsemusercelular = pfsemusercelular
        self.pfsemuserestado = pfsemuserestado
        self.pfsemusercreatedat = pfsemusercreatedat
        self.pfsemadminid = pfsemadminid
class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsemuserid','pfsemusernombres', 'pfsemuserapellidos', 'pfsemuseremail', 'pfsemuserdireccion', 'pfsemusercelular', 'pfsemuserestado', 'pfsemusercreatedat', 'pfsemadminid')

userSchema = UserSchema()
userSchema = UserSchema(many=True)

