from flask import Blueprint
from src.client.controller.clientControllerEmailMarketingSend import ClientControllerEmailMarketingSend
# client - router - email - marketing
crems= Blueprint('crems', __name__)
crems.route('/crems', methods=['GET', 'POST'])(ClientControllerEmailMarketingSend.onGetClientControllerEmailMarketingSend)

