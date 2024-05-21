from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
from src.client.model.clientModelProductoMarketing import ModelProductoMarketing
import pandas as pd

class ClientServiceProductMarketing:

    @classmethod
    def onGetClientServicioProductoMarketingAll(self, page):
        try:
            page = page
            pages = 10
            productoList = Producto.query.order_by(Producto.pfsemprodid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return productoList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def ongetClientServiceProductoName(self, search, page):
        try:
            page = page
            pages = 10
            productoList = Producto.query.filter(Producto.pfsemprodnombre.like(search)).paginate(per_page=pages,error_out=False)
            return productoList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')

    @classmethod
    def onGetClientServiceProductoMarketingSave(self, nombre, image, detalle, precio, stock, estado, createdAt, adminId):
        try:
            modelProductoMarketing = ModelProductoMarketing(0, nombre, image, detalle, precio, stock, estado, createdAt, adminId)
            newProductoMarketing = Producto(pfsemprodnombre = modelProductoMarketing.getnombre(),
                                            pfsemprodimage = modelProductoMarketing.getimage(),
                                            pfsemproddetalle = modelProductoMarketing.getdetalle(),
                                            pfsemprodprecio = modelProductoMarketing.getprecio(),
                                            pfsemprodstock = modelProductoMarketing.getstock(),
                                            pfsemprodestado = modelProductoMarketing.getestado(),
                                            pfsemprodcreatedat = modelProductoMarketing.getcreatedAt(),
                                            pfsemadminid = modelProductoMarketing.getadminId())
            
            if modelProductoMarketing.getnombre() != '' and modelProductoMarketing.getimage() and modelProductoMarketing.getdetalle() != '' and modelProductoMarketing.getprecio() != '' and modelProductoMarketing.getstock() != '' and modelProductoMarketing.getestado() != '' and modelProductoMarketing.getcreatedAt() != '' and modelProductoMarketing.getadminId():
                db.session.add(newProductoMarketing)
                db.session.commit()
                return True
            else:
                return False
        
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetClientServiceProductoMarketingOne(self, id):
        try:
            dataProducto = pd.Series(Producto.query.get(id))
            return dataProducto
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    
    @classmethod
    def onGetClientServiceProductoMarketingUpdate(self, id, nombre, image, detalle, precio, stock, estado, createdAt, adminId):
        try:
            modelProductoMarketing =  ModelProductoMarketing(id, nombre, image, detalle, precio, stock, estado, createdAt, adminId)
            producto = Producto.query.get(modelProductoMarketing.getid())
            producto.pfsemprodnombre = modelProductoMarketing.getnombre()
            producto.pfsemprodimage = modelProductoMarketing.getimage()
            producto.pfsemproddetalle = modelProductoMarketing.getdetalle()
            producto.pfsemprodprecio = modelProductoMarketing.getprecio()
            producto.pfsemprodstock = modelProductoMarketing.getstock()
            producto.pfsemprodestado = modelProductoMarketing.getestado()
            if  modelProductoMarketing.getid() != '' and modelProductoMarketing.getnombre() != '' and modelProductoMarketing.getimage() != '' and modelProductoMarketing.getdetalle() != '' and modelProductoMarketing.getprecio() != '' and modelProductoMarketing.getstock() != '' and modelProductoMarketing.getestado():
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetClientServiceProductoMarketingDelete(self, id):
        try:
            producto = Producto.query.get(id)
            producto.pfsemprodestado = 0
            if producto.pfsemprodestado != '':
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
