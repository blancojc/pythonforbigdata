import getpass
from gmail import Gmail

# Leemos los datos mediante la consola de entrada
my_gmail = input("Escribe tu Gmail: ")
my_gmail_password = getpass.getpass("Password: ")
list_dest_email = input("Introduce una lista con los emails de los destinatarios: ")
asunto = input("Asunto del email: ")
msg = input("Mensaje a enviar: ")

my_gmail = Gmail( my_gmail, my_gmail_password )
for dest_email in list_dest_email.split(',') :
    dest_email_cleaned = dest_email.strip()
    try :
        my_gmail.send_message( dest_email_cleaned, msg, asunto )
        print("Email enviado a %s" % dest_email_cleaned )
    except Exception as err :
        print("Error enviado el email a %s. " % dest_email_cleaned + str( err ) )
my_gmail.quit()

