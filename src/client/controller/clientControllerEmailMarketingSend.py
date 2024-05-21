from flask import render_template as render, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from src.client.services.clientServiceEmailMarketingSend import ClientServiceEmailMarketingSend
from src.client.form.clientFormProducto import ClientFormProductowtf
from flask_login import current_user
from datetime import datetime
class ClientControllerEmailMarketingSend():

    def onGetClientControllerEmailMarketingSend():
        try:
            if current_user.is_authenticated:
                ClientServiceEmailMarketingSend.onGetClientServiceSend()
                return redirect(url_for('crem.onGetClientControllerEmailMarketingView'))
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
