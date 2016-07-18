import smtplib

def send_email( ):
    """
    Funcion para el envio de correos desde una cuenta de Gmail
    """
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login( "XXSDF@gmail.com", "AWQEF" )
    text_to_send = "Subject: %s\n\n%s" % ( "Hola", "Es una prueba" )
    session.sendmail( "XXSDF@gmail.com", "QWEDF@gmail.com", text_to_send )    
    session.quit()

send_email( )
