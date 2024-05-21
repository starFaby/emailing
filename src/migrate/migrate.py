import sys
from datetime import datetime
from src.database.database import *
def createDB():
    db.drop_all()
    db.create_all()

def initDB():
    createDB()
    admin = Admin( 
        pfsadmincedula = "1725302705",
        pfsadminnombres = "edgar fabian",
        pfsadminapellidos = "estrella guambuguete",
        pfsadminusername = "starfaby",
        pfsadminemail = "star._faby@hotmail.com",
        pfsadminpassword = "star123",
        pfsadmindireccion = "Ferroviaria Media Adrian Navarro S11-82 y puna", 
        pfsadmincellphone = "0983856136", 
        pfsadminphone = "022647002", 
        pfsadminisadmin = True,
        pfsadminavatar = "https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1638923678/starfaby_uqbwru.jpg",
        pfsadminestado = 1,
        pfsadmincreatedat = datetime.now()
    )
    admin.onGetSetPassword(admin.pfsadminpassword)
    db.session.add(admin)
    db.session.commit()  
    return 'base de datos creado existosamente' 