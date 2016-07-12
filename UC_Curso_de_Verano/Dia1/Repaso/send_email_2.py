import smtplib
# Podeis encontrar mas informacion sobre get pass en :
# https://docs.python.org/3/library/getpass.html
import getpass

def send_email( cuenta_gmail, password, email_destinatario, mensaje ):
    """
    Funcion para el envio de correos desde una cuenta de Gmail
    """
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login( cuenta_gmail, password )
    session.sendmail( cuenta_gmail, email_destinatario, mensaje )
    session.quit()

# Leemos los datos mediante la consola de entrada
my_gmail = input("Escribe tu Gmail: ")
my_gmail_password = getpass.getpass("Password: ")
dest_email = input("Email del destinatario: ")
msg = input("Mensaje a enviar: ")

send_email( my_gmail, my_gmail_password, dest_email, msg )
