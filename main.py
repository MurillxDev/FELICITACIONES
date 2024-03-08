from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.units import inch  # Import inch unit here

# Función para crear el PDF
def create_pdf(file_name, img_path, teacher_name, rector_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, f"Felicitación de Cumpleaños")
    c.drawString(100, 730, f"Fecha y hora de creación: {datetime.now()}")
    c.drawString(100, 700, f"Estimado {teacher_name}:")
    c.drawString(100, 680, f"¡En nombre de la comunidad educativa, el rector {rector_name} te desea")
    c.drawString(100, 660, "un feliz cumpleaños! Que este día esté lleno de alegría, amor y")
    c.drawString(100, 640, "bendiciones. ¡Gracias por tu dedicación y compromiso con la educación!")
    c.drawString(100, 620, "Atentamente,")
    c.drawString(100, 600, f"{rector_name}")

    # Añadir la imagen al centro del PDF
    img = Image(img_path, width=3*inch, height=3*inch)
    img.drawOn(c, 150, 400)

    c.save()

# Función para enviar el PDF por correo electrónico
def send_email(email_from, email_to, subject, attachment_path):
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

# Datos del docente y el rector
teacher_name = "Profesor(a) Ejemplo"
rector_name = "Nombre del Rector"
pdf_file_name = "felicitacion_cumpleanos.pdf"
img_path = "C:/Users/santy/OneDrive/Escritorio/CORREO/imagen1.jpg"

# Crear el PDF
create_pdf(pdf_file_name, img_path, teacher_name, rector_name)

# Configuración del correo electrónico
email_from = "victorramos10050@gmail.com"
email_to = "carlos.mmurillo@alumnos.udg.mx"
subject = "Felicitación de Cumpleaños"
# Enviar el correo electrónico con el PDF adjunto
send_email(email_from, email_to, subject, pdf_file_name)

print("Correo electrónico enviado exitosamente con la felicitación de cumpleaños adjunta.")
