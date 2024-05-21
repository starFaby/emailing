from flask import Blueprint
from src.admin.controller.adminControllerUser import AdminControllerUser
# admin - categoria - caso
aru= Blueprint('aru', __name__)
aru.route('/aru', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerUser.onGetAdminControllerUserViewList)
aru.route('/aru/<int:page>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserViewList)
aru.route('/arums', methods=['GET', 'POST'])(AdminControllerUser.onGetClientControllerUserMarketingModalS)
aru.route('/arus', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserSave)
aru.route('/arumu/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserModalUpdateView)
aru.route('/aruu', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserUpdate)
aru.route('/arud/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserDelete)

