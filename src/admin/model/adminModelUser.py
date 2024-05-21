class AdminModelUser():

    def __init__(self, id, nombres, apellidos, email, direccion, celular, estado, createdAt, adminId):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        self.celular = celular
        self.estado = estado
        self.createdAt = createdAt
        self.adminId = adminId
    
        
    #--------------------
    #--------------------
    # get y set id
    #---------------------
    #---------------------
    def getid(self):
        return self.id
    
    def setid(self, id):
        self.id = id

    #--------------------
    #--------------------
    # get y set nombres
    #---------------------
    #---------------------
    def getnombres(self):
        return self.nombres
    
    def setnombres(self, nombres):
        self.nombres = nombres

    #--------------------
    #--------------------
    # get y set apellidos
    #---------------------
    #---------------------
    def getapellidos(self):
        return self.apellidos
    
    def setapellidos(self, apellidos):
        self.apellidos = apellidos

    #--------------------
    #--------------------
    # get y set email
    #---------------------
    #---------------------
    def getemail(self):
        return self.email
    
    def setemail(self, email):
        self.email = email

    #--------------------
    #--------------------
    # get y set direccion
    #---------------------
    #---------------------
    def getdireccion(self):
        return self.direccion
    
    def setdireccion(self, direccion):
        self.direccion = direccion

    #--------------------
    #--------------------
    # get y set celular
    #---------------------
    #---------------------
    def getcelular(self):
        return self.celular
    
    def setcelular(self, celular):
        self.celular = celular

    #--------------------
    #--------------------
    # get y set estado
    #---------------------
    #---------------------
    def getestado(self):
        return self.estado
    
    def setestado(self, estado):
        self.estado = estado

    #--------------------
    #--------------------
    # get y set createdAt
    #---------------------
    #---------------------
    def getcreatedAt(self):
        return self.createdAt
    
    def setcreatedAt(self, createdAt):
        self.createdAt = createdAt

    #--------------------
    #--------------------
    # get y set adminId
    #---------------------
    #---------------------
    def getadminId(self):
        return self.adminId
    
    def setadminId(self, adminId):
        self.adminId = adminId

    #--------------------
    #--------------------
    # get y set Json
    #---------------------
    #---------------------
    def ProductoMarketingInJason(self):
        
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'image' : self.image,
            'detalle' : self.detalle,
            'precio' : self.precio,
            'stock' : self.stock,
            'estado' : self.estado,
            'createdAt' : self.createdAt,
            'adminId' : self.adminId
        }