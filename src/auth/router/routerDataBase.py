from flask import Blueprint
from src.migrate.migrate import initDB

ardbem= Blueprint('ardbem', __name__)

ardbem.route('/ardbem', methods=['GET'])(initDB)

