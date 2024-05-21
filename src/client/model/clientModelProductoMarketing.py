class ModelProductoMarketing():

    def __init__(self, id, nombre, image, detalle, precio, stock, estado, createdAt, adminId):
        self.id = id
        self.nombre = nombre
        self.image = image
        self.detalle = detalle
        self.precio = precio
        self.stock = stock
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
    # get y set nombre
    #---------------------
    #---------------------
    def getnombre(self):
        return self.nombre
    
    def setnombre(self, nombre):
        self.nombre = nombre

    #--------------------
    #--------------------
    # get y set image
    #---------------------
    #---------------------
    def getimage(self):
        return self.image
    
    def setimage(self, image):
        self.image = image

    #--------------------
    #--------------------
    # get y set detalle
    #---------------------
    #---------------------
    def getdetalle(self):
        return self.detalle
    
    def setdetalle(self, detalle):
        self.detalle = detalle

    #--------------------
    #--------------------
    # get y set precio
    #---------------------
    #---------------------
    def getprecio(self):
        return self.precio
    
    def setprecio(self, precio):
        self.precio = precio

    #--------------------
    #--------------------
    # get y set stock
    #---------------------
    #---------------------
    def getstock(self):
        return self.stock
    
    def setstock(self, stock):
        self.stock = stock

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