import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from reportlab.lib.units import inch
#!pip install smtplib

# Crea la conexión SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)

correo = 'martinezcristhoper538@gmail.com'
pas ='xmjh lofb dmhm syjy'
# Inicia sesión en tu cuenta de Gmail
server.starttls()

server.login(correo, pas)

# Definir el remitente y destinatario del correo electrónico
remitente = "martinezcristhoper538@gmail.com"
destinatario = "cristopher.celestino25@gmail.com"

# Crear el mensaje del correo electrónico
mensaje = email.mime.multipart.MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = "Correo electrónico con archivo adjunto"

# Añadir el cuerpo del mensaje
cuerpo = "Hola,\n\nEste es un mensaje de prueba enviado desde Python con un archivo adjunto.\n\nSaludos,\n Cristopher"
mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))


def create_pdf(file_name):
    # Crear el lienzo del PDF
    pdf_canvas = canvas.Canvas(file_name, pagesize=letter)

    # Definir el encabezado
    header_text = "Ejemplo de PDF con Encabezado, Imagen y Frase"
    pdf_canvas.drawString(30, 750, header_text)

    # Insertar imagen
    img = Image("/file.png", width=3*inch, height=3*inch)
    img.drawOn(pdf_canvas, 100, 600)

    # Agregar frase
    frase = "¡Hola, mundo PDF!"
    pdf_canvas.drawString(100, 550, frase)

    # Guardar el PDF
    pdf_canvas.save()

# Llamar a la función para crear el PDF
create_pdf("ejemplo.pdf")

# Añadir el archivo Excel como adjunto
ruta_archivo = '/content/ejemplo.pdf'
archivo = open(ruta_archivo, 'rb')
adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
adjunto.set_payload((archivo).read())
email.encoders.encode_base64(adjunto)
adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
mensaje.attach(adjunto)

# Convertir el mensaje a texto plano
texto = mensaje.as_string()

# Enviar el correo electrónico
server.sendmail(remitente, destinatario, texto)

# Cerrar la conexión SMTP
server.quit()