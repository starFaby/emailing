from flask import Blueprint
from src.client.controller.clientControllerEmailMarketing import ClientControllerEmailMarketing
# client - router - email - marketing
crem= Blueprint('crem', __name__)
crem.route('/crem', methods=['GET', 'POST'])(ClientControllerEmailMarketing.onGetClientControllerEmailMarketingView)

