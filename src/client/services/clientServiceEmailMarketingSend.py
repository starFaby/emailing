from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.client.model.clientModelProductoMarketing import ModelProductoMarketing
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import threading
import smtplib, ssl
import pandas as pd
from random import randint
import time

class ClientServiceEmailMarketingSend():

    def onGetClientServiceSend():
        segundos = 3
        emailUser = pd.Series(User.query.all())
        for emus in emailUser:
            ClientServiceEmailMarketingSend.onGetClientServiceSendContent(emus.pfsemuseremail)
            time.sleep(segundos)

    def onGetClientServiceSendContent(emailUser):
        arreglo = []
        productouno = ''
        productodos = ''
        productotres = ''
        productocuatro = ''
        emailEmisor = 'reaveplayer@gmail.com'
        emailcontraseña = 'hlowzcxappqgaliy'

        emailReceptor = 'efg.estrella@yavirac.edu.ec'

        asunto = 'Publicidad de mercaderia Automatismos Brito'

        mensaje = MIMEMultipart('alternative')
        mensaje['From'] = emailEmisor
        mensaje['to'] = emailUser
        mensaje['Subject'] = asunto

        productMarketing = ClientServiceEmailMarketingSend.onGetClientServicesEmailMarketingProductVarios()
        for item in productMarketing:
            arreglo.append(item)
        
        print(arreglo)

        print(arreglo[0].pfsemprodimage)

        maquinaVending = 'https://www.vendingecuador.com/wp-content/uploads/2021/01/maquina-snacks.jpg'

        html = f"""
                <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>

        <body>
            <section style="width: 100%;">
                <header style="width: 100%; text-align: center; background-color: #e5e5e5;">
                    <h1 style="font-size: 5vw;">Automatismos Brito</h1>
                </header>
                <main style="width: 100%;">
                    <div style="float: left; width: 20%;">
                        <div style="width: 100%; text-align: center;">
                            <div style="width: 100%; margin-top: 5px; margin-bottom: 5px;">
                                <a href="https://vabautobrito.pythonanywhere.com/"><button
                                        style="background-color: #e5e5e5; padding: 0px;  width: 100%; font-size: 1vw;">Automatismos
                                        Brito</button></a>
                            </div>
                            <div style="width: 100%; color: red;">
                                <h6>Otros Servicios</h6>
                            </div>
                            <div style="width: 100%; margin-top: 5px; margin-bottom: 5px;">
                                <a href=""><button
                                        style="background-color: #e5e5e5; padding: 0px;  width: 100%; font-size: 1vw;">
                                        Abogados</button></a>
                            </div>
                            <div style="width: 100%; margin-top: 5px; margin-bottom: 5px;">
                                <a href=""><button
                                        style="background-color: #e5e5e5; padding: 0px;  width: 100%; font-size: 1vw;">
                                        Peluqueria</button></a>
                            </div>
                            <div style="width: 100%; margin-top: 5px; margin-bottom: 5px;">
                                <a href=""><button
                                        style="background-color: #e5e5e5; padding: 0px;  width: 100%; font-size: 1vw;">
                                        Electrico</button></a>
                            </div>
                            <div style="width: 100%; margin-top: 5px; margin-bottom: 5px;">
                                <a href=""><button
                                        style="background-color: #e5e5e5; padding: 0px;  width: 100%; font-size: 1vw;">star
                                        store</button></a>
                            </div>
                        </div>
                    </div>
                    <div style="float: left; width: 60%;">
                        <div style="text-align: center;">
                            <span style="font-size: 3vw;  font-weight: bold;">Articulos</span>
                        </div>
                        <div style="width: 100%;">
                                <img style="width: 15vw; height: 15vw; float: left; margin: 5px;"
                                    src="{ arreglo[0].pfsemprodimage }"
                                    alt="">
                                <img style="width: 15vw; height: 15vw; float: left; margin: 5px;"
                                    src="{ arreglo[1].pfsemprodimage }"
                                    alt="">
                                <img style="width: 15vw; height: 15vw; float: left; margin: 5px;"
                                    src="{ arreglo[2].pfsemprodimage }"
                                    alt="">
                                <img style="width: 15vw; height: 15vw; float: left; margin: 5px;"
                                    src="{ arreglo[3].pfsemprodimage }"
                                    alt="">
                        </div>
                    </div>
                    <div style="float: left; width: 20%; font-size: 2vw;">
                        <div style="width: 100%; text-align: center; background-color: #e5e5e5; margin-bottom: 5px;">
                            <span style="font-size: 2vw; font-weight: bold;">Nosotros</span>
                        </div>
                        <div style="background-color: #e5e5e5;">
                            <p style="text-align: justify;">
                                Es una Entidad que se dedica a la publicidad de productos de una empresa, como tambien otros
                                servicios para mantener informado a los clientes de las nuevas ofertas.
                            </p>
                        </div>
                    </div>
                </main>
                <footer style="width: 100%; text-align: center; clear: both; background-color: #e5e5e5;">
                    <h1>© copyright Automatismos Brito</h1>
                </footer>
            </section>
        </body>

        </html>
        """




        parteHtml = MIMEText(html, 'html')

        mensaje.attach(parteHtml)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(emailEmisor, emailcontraseña)
            smtp.sendmail(emailEmisor, emailReceptor, mensaje.as_string())
    
    def onGetClientServicesEmailMarketingProductVarios():
        productMarketing = []
            
        cantProductMarketing = pd.Series(Producto.query.all())
        cantpm =  cantProductMarketing.count()
        uno = randint(1, cantpm )
        productMarketingUno = Producto.query.get(uno)
        dos = randint(1, cantpm )
        productMarketingDos = Producto.query.get(dos)

        tres = randint(1, cantpm )
        productMarketingDTres = Producto.query.get(tres)

        cuatro = randint(1, cantpm )
        productMarketingCuatro = Producto.query.get(cuatro)

        productMarketing.append(productMarketingUno)
        productMarketing.append(productMarketingDos)
        productMarketing.append(productMarketingDTres)
        productMarketing.append(productMarketingCuatro)
            

        return productMarketing
    
