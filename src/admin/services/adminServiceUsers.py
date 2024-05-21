from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
from src.admin.model.adminModelUser import AdminModelUser
import pandas as pd

class AdminServiceUser:

    @classmethod
    def onGetAdminServiceUser(self, page):
        try:
            page = page
            pages = 10
            userList = User.query.order_by(User.pfsemuserid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceUserName(self, search, page):
        try:
            page = page
            pages = 10
            userList = User.query.filter(User.pfsemusernombres.like(search)).paginate(per_page=pages,error_out=False)
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')

    @classmethod
    def onGetAdminServiceUserSave(self, nombres, apellidos, email, direccion, celular, estado, createdAt, adminId):
        try:
            modelUserMarketing = AdminModelUser(0, nombres, apellidos, email, direccion, celular, estado, createdAt, adminId)
            newUser = User( pfsemusernombres = modelUserMarketing.getnombres(),
                            pfsemuserapellidos = modelUserMarketing.getapellidos(),
                            pfsemuseremail = modelUserMarketing.getemail(),
                            pfsemuserdireccion = modelUserMarketing.getdireccion(),
                            pfsemusercelular = modelUserMarketing.getcelular(),
                            pfsemuserestado = modelUserMarketing.getestado(),
                            pfsemusercreatedat = modelUserMarketing.getcreatedAt(),
                            pfsemadminid = modelUserMarketing.getadminId())
            
            if modelUserMarketing.getnombres() != '' and modelUserMarketing.getapellidos() and modelUserMarketing.getemail() != '' and modelUserMarketing.getdireccion() != '' and modelUserMarketing.getcelular() != '' and modelUserMarketing.getestado() != '' and modelUserMarketing.getcreatedAt() != '' and modelUserMarketing.getadminId():
                db.session.add(newUser)
                db.session.commit()
                return True
            else:
                return False
        
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    #---------------------------- 
    #---------------------------- 
    #Metodo para traer aun usuario
    #---------------------------- 
    #-----------------------------   
    @classmethod
    def onGetAdminServiceUserOne(self, id):
        try:
            dataUser = pd.Series(User.query.get(id))
            return dataUser
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    
    @classmethod
    def onGetAdminServiceUpdate(self, id, nombres, apellidos, email, direccion, celular, estado, createdAt, adminId):
        try:
            adminModelUser =  AdminModelUser(id, nombres, apellidos, email, direccion, celular, estado, createdAt, adminId)
            user = User.query.get(adminModelUser.getid())
            user.pfsemusernombres = adminModelUser.getnombres()
            user.pfsemuserapellidos = adminModelUser.getapellidos()
            user.pfsemuseremail = adminModelUser.getemail()
            user.pfsemuserdireccion = adminModelUser.getdireccion()
            user.pfsemusercelular = adminModelUser.getcelular()
            user.pfsemuserestado = adminModelUser.getestado()
            if  adminModelUser.getid() != '' and adminModelUser.getnombres() != '' and adminModelUser.getapellidos() != '' and adminModelUser.getemail() != '' and adminModelUser.getdireccion() != '' and adminModelUser.getcelular() != '' and adminModelUser.getestado():
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceUserDelete(self, id):
        try:
            user = User.query.get(id)
            user.pfsemuserestado = 0
            if user.pfsemuserestado != '':
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
