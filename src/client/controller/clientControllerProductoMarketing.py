from flask import render_template as render, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from src.client.form.clientFormProducto import ClientFormProductowtf
from flask_login import current_user
from src.client.services.clientServiceProductoMarketing import ClientServiceProductMarketing
from datetime import datetime


class ClientControllerProductoMarketing:

    def onGetClientControllerProductoMarketingView(page):
        try:
            if current_user.is_authenticated:
                page = page
                producto = ClientServiceProductMarketing.onGetClientServicioProductoMarketingAll(page)
                if producto != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        producto = ClientServiceProductMarketing.ongetClientServiceProductoName(search, page)
                        return render("client/clientProductoMarketing.html", producto=producto, tag = tag)
                    else:
                        flash('producto Listadas', category='success')
                        return render("client/clientProductoMarketing.html", producto=producto)
                else:
                    flash('No existe producto', category='success')
                    return render("client/clientProductoMarketing.html", producto=producto)
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
    
    def onGetClientControllerProductoMarketingModal():
        producto = []
        context = {
            'formProducto': ClientFormProductowtf(),
            'faby':'star',
            "save": True,
            "udpate": False,
            "producto": producto
        }
        try: 
            return render("client/clientProductoMarketing.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
        
    def onGetClientControllerProductoMarketingSave():
        try: 
            if current_user.is_authenticated:
                formProducto = ClientFormProductowtf()
                if formProducto.validate_on_submit():
                    id = formProducto.id.data
                    nombre = formProducto.nombre.data
                    image = formProducto.image.data
                    detalle = formProducto.detalle.data
                    precio = formProducto.precio.data
                    stock = formProducto.stock.data
                    estado = formProducto.estado.data
                    createdAt = datetime.now()
                    adminId = current_user.adminId
                    cspm = ClientServiceProductMarketing.onGetClientServiceProductoMarketingSave(nombre, image, detalle, precio, stock, estado, createdAt, adminId)
                    if cspm is True:
                        flash('Producto Guardado', category='success')
                        print("Ingreso de datos exitosamente")
                        return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))
                    else:
                        print("Error al registrar los datos")
                        return redirect(url_for('crpm.onGetClientControllerProductoMarketingView')) 
                else:
                    print("Datos Vacios mijin")    
                    return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    
    def onGetClientControllerProductoMarketingUpdateView(id):
        producto = []
        dataProducto = []

        resultData = ClientServiceProductMarketing.onGetClientServiceProductoMarketingOne(id)
        for repro in resultData:
            dataProducto = repro
        context = {
            'formProducto': ClientFormProductowtf(),
            'faby':'star',
            "save": False,
            "udpate": True,
            "producto": producto,
            "dataProducto": dataProducto
        }
        try: 
            return render("client/clientProductoMarketing.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    
    def onGetClientControllerProductoMarketingUpdate():
        try:
            if current_user.is_authenticated:
                formProducto = ClientFormProductowtf()
                if formProducto.validate_on_submit():
                    id = formProducto.id.data
                    nombre = formProducto.nombre.data
                    image = formProducto.image.data
                    detalle = formProducto.detalle.data
                    precio = formProducto.precio.data
                    stock = formProducto.stock.data
                    estado = formProducto.estado.data
                    createdAt = datetime.now() 
                    adminId = current_user.adminId
                    productoUpdate = ClientServiceProductMarketing.onGetClientServiceProductoMarketingUpdate(id, nombre, image, detalle, precio, stock, estado, createdAt, adminId)
                    if productoUpdate is True:
                        return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))
                    else:
                        return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))
                else:
                    print("Datos Vacios")
                    return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))

            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
    
    def onGetClientControllerProductoMarketingDelete(id):
        try:
            formProducto = ClientFormProductowtf()
            if current_user.is_authenticated:
                producto = ClientServiceProductMarketing.onGetClientServiceProductoMarketingDelete(id)
                if producto is True:
                    return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))
                else:
                    return redirect(url_for('crpm.onGetClientControllerProductoMarketingView'))
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 