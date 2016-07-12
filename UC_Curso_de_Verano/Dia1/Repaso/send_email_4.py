import smtplib
import getpass

class Gmail(object):
    """
    Clase para enviar correos de texto desde una cuenta de gmail
    """

    SERVER = 'smtp.gmail.com'
    PORT   = 587

    def __init__(self, email, password):
        self.email = email
        self.password = password
        session = smtplib.SMTP( self.SERVER, self.PORT )        
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(self.email, self.password)
        self.session = session
 
    def quit(self):
        """Quit session"""
        self.session.quit()

    def send_message(self, email_destinatario, mensaje, asunto = ""):
        """Send an email"""
        text_to_send = "Subject: %s\n\n%s" % ( asunto, mensaje)
        self.session.sendmail( self.email, email_destinatario, text_to_send )

# Leemos los datos mediante la consola de entrada
my_gmail = input("Escribe tu Gmail: ")
my_gmail_password = getpass.getpass("Password: ")
dest_email = input("Email del destinatario: ")
asunto = input("Asunto del email: ")
msg = input("Mensaje a enviar: ")

try :
    my_gmail = Gmail( my_gmail, my_gmail_password )
    my_gmail.send_message( dest_email, msg, asunto )
    print("Email enviado correctamente")
except Exception as err :
    print("Error enviando el correo" + str(err) )
# Cambio en la estructura try/except
finally :
    my_gmail.quit()
