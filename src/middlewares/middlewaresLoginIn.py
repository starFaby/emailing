from flask_login import UserMixin
from src.auth.services.serviceAuth import ServiceAuth
class UserModel(UserMixin):
    def __init__(self, userData):
        self.id = userData.pfsadminusername
        self.adminId = userData.pfsadminid
        self.password = userData.pfsadminpassword
        self.email = userData.pfsadminemail
        self.avatar = userData.pfsadminavatar
        self.isadmin = userData.pfsadminisadmin
        self.estado = userData.pfsadminestado
        
    @staticmethod
    def get(pfsadminusername):
        userData = ServiceAuth.onGetUserByUserName(pfsadminusername = pfsadminusername)
        return UserModel(userData)