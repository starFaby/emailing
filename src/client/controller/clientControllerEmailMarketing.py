from flask import render_template as render, request
from sqlalchemy.exc import SQLAlchemyError
from src.client.services.clientServiceEmailMarketing import ClientServiceEmailMarketing
from flask_login import current_user

class ClientControllerEmailMarketing:

    def onGetClientControllerEmailMarketingView():
        try:
            if current_user.is_authenticated:
                productMarketing = ClientServiceEmailMarketing.onGetClientServiceEmailMarketingProductSave()
                context = {
                    'productMarketing':productMarketing
                }
                return render("client/clientEmailMarketing.html", **context)
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 

    def onGetClientControllerEmailMarketingSend():
        try:
            if current_user.is_authenticated:
                return render("client/clientEmailMarketing.html")
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)   
        