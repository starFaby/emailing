from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
import datetime
from src.client.model.clientModelProductoMarketing import ModelProductoMarketing
import pandas as pd
import numpy as np
from random import randint

class ClientServiceEmailMarketing:

    @classmethod
    def onGetClientServiceEmailMarketingProductSave(self):
        try:
            productMarketing = []
            
            cantProductMarketing = pd.Series(Producto.query.all())
            cantpm =  cantProductMarketing.count()
            if cantpm >= 1:

                uno = randint(1, cantpm )
                productMarketingUno = Producto.query.get(uno)

                dos = randint(1, cantpm )
                productMarketingDos = Producto.query.get(dos)

                tres = randint(1, cantpm )
                productMarketingDTres = Producto.query.get(tres)

                cuatro = randint(1, cantpm )
                productMarketingCuatro = Producto.query.get(cuatro)

                productMarketing.append(productMarketingUno)
                productMarketing.append(productMarketingDos)
                productMarketing.append(productMarketingDTres)
                productMarketing.append(productMarketingCuatro)
                
                cantProductMarketing = pd.Series(productMarketing)
                
                return cantProductMarketing
            else:
                return cantProductMarketing
            
            
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)