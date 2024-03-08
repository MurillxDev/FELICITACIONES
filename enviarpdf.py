from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from reportlab.lib.units import inch
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Función para crear el PDF
def create_pdf(file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, "Ejemplo de PDF Dinámico")
    c.drawString(100, 730, f"Fecha y hora de creación: {datetime.now()}")
    img = Image("D:/Uni/Metodologias de desarrollo/descargar.png", width=3*inch, height=3*inch)
    img.drawOn(c, 100, 600)
    mensaje = "¡Hola, mundo PDF!"
    c.drawString(100, 550, mensaje)

    c.save()
    

# Función para enviar el PDF por correo electrónico
def send_email(email_from, email_to, subject, body, attachment_path):
    # Configuración del correo electrónico
    email_server = "smtp.gmail.com"
    email_port = 587
    email_user = "victorramos10050@gmail.com"
    email_password = "irlg ituc ouah vrwy"

    # Configuración del mensaje
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF al mensaje
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )
    msg.attach(part)

    # Iniciar sesión en el servidor SMTP y enviar el correo electrónico
    with smtplib.SMTP(email_server, email_port) as server:
        server.starttls()
        server.login(email_user, email_password)
        server.send_message(msg)

# Crear el PDF
pdf_file_name = "ejemplo.pdf"
create_pdf(pdf_file_name)

# Configuración del correo electrónico
email_from = "victorramos10050@gmail.com"
email_to = "victorramos10050@gmail.com"
subject = "PDF Dinámico"
body = "Adjunto encontrarás el PDF dinámico generado automáticamente."

# Enviar el correo electrónico con el PDF adjunto
send_email(email_from, email_to, subject, body, pdf_file_name)

print("Correo electrónico enviado exitosamente con el PDF adjunto.")
