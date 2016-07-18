import smtplib
# Podeis encontrar mas informacion sobre el paquete smtplib en :
# https://docs.python.org/3/library/smtplib.html

# Creamos un objeto session para el envio the emails
session = smtplib.SMTP('smtp.gmail.com', 587)
# Nos identificamos contra el cliente smtp de gmail
session.ehlo()
# Indicamos que nuestra conexion sera encriptada
session.starttls()
# Nos volvemos a identificar
session.ehlo()
# Nos logueamos en nuestra cuenta de gmail
session.login( "XXXX@gmail.com", "Xqwef" )
# Enviamos un mensaje desde nuestra cuenta de correo (XXXX@gmail.com) a otra ("XYXX@gmail.com)
session.sendmail( "XXXX@gmail.com", "XYXX@gmail.com", "Subject: Hola\n\nEsto es una prueba")
# Cerramos la conexion 
session.quit()
