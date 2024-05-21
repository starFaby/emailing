#System

from flask import Flask
from flask_login import LoginManager
from .config.config import Config
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from src.database.database import db, ma
#Admin routes
from src.admin.router.adminRouterUsers import aru
#Client routes
from src.client.router.clientRouterEmailMarketing import crem
from src.client.router.clientRouterProductoMarketing import crpm
from src.client.router.clientRouterEmailMarketingSend import crems
# Auth routes
from src.auth.router.routerAuth import rauth
from src.auth.router.routerLoginIn import rlgn
from src.auth.router.routerDataBase import ardbem
from src.auth.router.routerLogout import rlgt


# middlewares
from src.middlewares.middlewaresLoginIn import UserModel

loginManager = LoginManager()
loginManager.loginView = 'auth.controller.controllerLoginIn'

@loginManager.user_loader
def loadUser(username):
    return UserModel.get(username)

def apprun():
    #Sistem
    app = Flask(__name__)
    app.config.from_object(Config)

    #   Auth
    app.register_blueprint(rauth)
    app.register_blueprint(rlgn)
    app.register_blueprint(ardbem)
    app.register_blueprint(rlgt)
    #   Admin
    app.register_blueprint(aru)

    #   Client
    app.register_blueprint(crem)
    app.register_blueprint(crpm)
    app.register_blueprint(crems)
    
    #Sistem
    loginManager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    return app



