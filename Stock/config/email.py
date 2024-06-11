import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

smtp_server = ''
smtp_port = 587
smtp_user = ''
smtp_password = ''
email_destinatario = ['', '']

# Función para enviar registro al correo.
def enviar_correo(asunto='Registro de Actualización', cuerpo='Procesamiento completado'):
    try:
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = ', '.join(email_destinatario)
        msg['Subject'] = asunto

        # Añadir cuerpo del mensaje
        msg.attach(MIMEText(cuerpo, 'plain'))

        with open('Resumen-Stock.log', 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= Resumen-Stock.log")
            msg.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()
        logging.info(f"Correo enviado exitosamente a {', '.join(email_destinatario)}")
    except Exception as e:
        logging.error(f"Error al enviar el correo: {e}")
        print(f"Error al enviar el correo a {', '.join(email_destinatario)}: {e}")
