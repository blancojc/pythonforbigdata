import smtplib

def send_email():
    """
    Funcion para el envio de correos desde una cuenta de Gmail
    """
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login( "josecarlosblancoreal@gmail.com", "U1olnlalee" )
    session.ehlo()
    session.sendmail( "josecarlosblancoreal@gmail.com", "josecarlosblancoreal@gmail.com", "Subject: Hola\n\nEsto es una prueba")
    session.quit()

send_email()
