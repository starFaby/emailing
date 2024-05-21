import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailMarketing:

    def onGetEmailEmailMarketing(emailUser):
        emailEmisor = 'reaveplayer@gmail.com'
        emailcontraseña = 'hlowzcxappqgaliy'
        emailReceptor = emailUser

        asunto = 'Empresa Automatismo Brito(kits Electronicos)'

        mensaje = MIMEMultipart('alternative')
        mensaje['From'] = emailEmisor
        mensaje['to'] = emailReceptor
        mensaje['Subject'] = asunto


        html = """"""

        with open('email.html','r') as archivo:
            html = archivo.read()


        parteHtml = MIMEText(html, 'html')

        mensaje.attach(parteHtml)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(emailEmisor, emailcontraseña)
            smtp.sendmail(emailEmisor, emailReceptor, mensaje.as_string())