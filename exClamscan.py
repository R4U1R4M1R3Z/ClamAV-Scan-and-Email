import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de los datos de correo electrónico
imap_server = 'servidor.correo.com'
imap_port = 143
smtp_username = 'usuario@correo.com'
smtp_password = 'contraseña'
sender_email = 'usuario@correo.com'
recipient_email = 'usuario@correo.com'

# Ejecutar el comando clamscan -r /
process = subprocess.Popen(['clamscan', '-r', '/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Obtener el resumen del escaneo
scan_summary = output.decode('utf-8').split('----------- SCAN SUMMARY -----------')[1]

# Crear el mensaje de correo electrónico
msg = MIMEMultipart()
msg['Subject'] = 'Resultado del escaneo de ClamAV'
msg['From'] = sender_email
msg['To'] = recipient_email

# Agregar el resumen del escaneo al cuerpo del correo
body = MIMEText(scan_summary.strip())
msg.attach(body)

# Adjuntar el resultado completo como archivo de texto
attachment = MIMEText(output.decode('utf-8'))
attachment.add_header('Content-Disposition', 'attachment', filename='resultado.txt')
msg.attach(attachment)


# Configuración del servidor SMTP
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()
smtp.login(smtp_username, smtp_password)
smtp.send_message(msg)
smtp.quit()

print('Correo electrónico enviado exitosamente.')
