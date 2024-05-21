from flask import render_template as render, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from src.admin.form.adminFormUser import AdminFormUserWtf
from flask_login import current_user
from src.admin.services.adminServiceUsers import AdminServiceUser
from datetime import datetime


class AdminControllerUser:

    def onGetAdminControllerUserViewList(page):
        try:
            if current_user.is_authenticated:
                page = page
                userList = AdminServiceUser.onGetAdminServiceUser(page)
                if userList != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        userList = AdminServiceUser.onGetAdminServiceUserName(search, page)
                        return render("admin/adminUser.html", userList=userList, tag = tag)
                    else:
                        flash('producto Listadas', category='success')
                        return render("admin/adminUser.html", userList=userList)
                else:
                    return render("admin/adminUser.html", userList=userList)
            else:
                return render("auth/loginin.html")

        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
    
    def onGetClientControllerUserMarketingModalS():
        userList = []
        context = {
            'formUser': AdminFormUserWtf(),
            "save": True,
            "udpate": False,
            "userList": userList
        }
        try: 
            return render("admin/adminUser.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
        
    def onGetAdminControllerUserSave():
        try: 
            if current_user.is_authenticated:
                formUser = AdminFormUserWtf()
                if formUser.validate_on_submit():
                    nombres = formUser.nombres.data
                    apellidos = formUser.apellidos.data
                    email = formUser.email.data
                    direccion = formUser.direccion.data
                    celular = formUser.celular.data
                    estado = formUser.estado.data
                    createdAt = datetime.now()
                    adminId = current_user.adminId
                    cspm = AdminServiceUser.onGetAdminServiceUserSave(nombres, apellidos, email, direccion, celular, estado, createdAt, adminId)
                    if cspm is True:
                        flash('Usuario Guardado', category='success')
                        return redirect(url_for('aru.onGetAdminControllerUserViewList'))
                    else:
                        return 'Error al registrar'#render("client/clientProductoMarketing.html")  
                    
                return redirect(url_for('aru.onGetAdminControllerUserViewList'))
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    
    def onGetAdminControllerUserModalUpdateView(id):
        userList = []
        dataUser = []

        resultData = AdminServiceUser.onGetAdminServiceUserOne(id)
        for reuser in resultData:
            dataUser = reuser
        context = {
            'formUser': AdminFormUserWtf(),
            'faby':'star',
            "save": False,
            "update": True,
            "userList": userList,
            "dataUser": dataUser
        }
        try: 
            return render("admin/adminUser.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    
    def onGetAdminControllerUserUpdate():
        try:
            formUser = AdminFormUserWtf()
            if current_user.is_authenticated:
                if formUser.validate_on_submit():
                    id = formUser.id.data
                    nombres = formUser.nombres.data
                    apellidos = formUser.apellidos.data
                    email = formUser.email.data
                    direccion = formUser.direccion.data
                    celular = formUser.celular.data
                    estado = formUser.estado.data
                    createdAt = datetime.now() 
                    adminId = current_user.adminId
                    productoUpdate = AdminServiceUser.onGetAdminServiceUpdate(id, nombres, apellidos, email, direccion, celular, estado, createdAt, adminId)
                    if productoUpdate is True:
                        return redirect(url_for('aru.onGetAdminControllerUserViewList'))
                    else:
                        return redirect(url_for('aru.onGetAdminControllerUserViewList'))
                else:
                    return redirect(url_for('aru.onGetAdminControllerUserViewList'))

            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    
    def onGetAdminControllerUserDelete(id):
        try:
            if current_user.is_authenticated:
                user = AdminServiceUser.onGetAdminServiceUserDelete(id)
                if user is True:
                    return redirect(url_for('aru.onGetAdminControllerUserViewList'))
                else:
                    return redirect(url_for('aru.onGetAdminControllerUserViewList'))
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    """
    def onGetAdminControllerUserList():
        print("request.headers")
        print(request.headers)
        hasAccess = SecurityAuth.verifyAuthToken(request.headers)
        print(hasAccess)
        #if hasAccess:
        try:
            users = AdminServiceUser.ongetAdminServiceUser()
            if users is not None:
                return render("admin/adminUsers.html", users = users)
            else:
                return render("admin/adminUsers.html", users = users)
        except SQLAlchemyError as e:
                print("Error en Service User ", e)
                return render('errors/error500.html')    
        #else:
            #return render('errors/error401.html')
    """