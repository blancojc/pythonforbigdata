import smtplib

def send_email():
    """
    Funcion para el envio de correos desde una cuenta de Gmail
    """
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login( "XXXX@gmail.com", "Xqwef" )
    session.ehlo()
    session.sendmail( "XXXX@gmail.com", "XXXX@gmail.com", "Esto es una prueba")
    session.quit()

send_email()
