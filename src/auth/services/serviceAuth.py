import sys
from datetime import datetime
from flask import render_template as render, request, jsonify, redirect, url_for
from sqlalchemy.sql.elements import Null
from sqlalchemy.exc import SQLAlchemyError
from src.database.database import *

class ServiceAuth():
    
    def onGetUserByUserName(pfsadminusername):
        try:
            return Admin.query.filter_by(pfsadminusername = pfsadminusername).first()
        except SQLAlchemyError as e:
            print("error", e)
            return render('errors/error500.html')