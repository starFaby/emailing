from flask import Blueprint
from src.client.controller.clientControllerProductoMarketing import ClientControllerProductoMarketing
# client - router - email - marketing
crpm= Blueprint('crpm', __name__)
crpm.route('/crpm', methods=['GET', 'POST'], defaults={"page": 1})(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingView)
crpm.route('/crpm/<int:page>', methods=['GET', 'POST'])(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingView)
crpm.route('/crpmm', methods=['GET'])(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingModal)
crpm.route('/crpms', methods=['GET', 'POST'])(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingSave)
crpm.route('/crpmupv/<int:id>', methods=['GET'])(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingUpdateView)
crpm.route('/crpmupdate', methods=['GET', 'POST'])(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingUpdate)
crpm.route('/crpmdel/<id>', methods=['GET', 'POST'])(ClientControllerProductoMarketing.onGetClientControllerProductoMarketingDelete)


