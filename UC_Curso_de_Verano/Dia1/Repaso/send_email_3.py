import smtplib
import getpass

def send_email( cuenta_gmail, password, email_destinatario, mensaje, asunto = '' ):
    """
    Funcion para el envio de correos desde una cuenta de Gmail
    """
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login( cuenta_gmail, password )
    text_to_send = "Subject: %s\n\n%s" % ( asunto, mensaje )
    session.sendmail( cuenta_gmail, email_destinatario, text_to_send )
    session.quit()

# Leemos los datos mediante la consola de entrada
my_gmail = input("Escribe tu Gmail: ")
my_gmail_password = getpass.getpass("Password: ")
dest_email = input("Email del destinatario: ")
asunto = input("Asunto del email: ")
msg = input("Mensaje a enviar: ")

try :
    send_email( my_gmail, my_gmail_password, dest_email, msg, asunto )
    print("Email enviado correctamente")
except Exception as err :
    print("Error enviando el correo" + str(err) )

