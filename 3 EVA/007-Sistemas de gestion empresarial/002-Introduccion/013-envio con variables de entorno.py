# echo 'export RESEND_API_KEY="re_ZW13R3Nb_6T38wjHvEs1w34U8oDETTSN2"' >> ~/.bashrc

import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = "smtp.resend.com"
SMTP_PORT = 587         # 587 = STARTTLS, 465 = SSL
SMTP_USER = "resend"
SMTP_PASS = os.environ.get("RESEND_API_KEY")

if not SMTP_PASS:
    raise ValueError("RESEND_API_KEY no está definida")
    
msg = EmailMessage()
msg["From"] = "raxira8778@coswz.com"
msg["To"] = "tsarhiro@protonmail.com"
msg["Subject"] = "Esto es un ejercicio de clase"
msg.set_content("Hola esto es una prueba desde Python.\n")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")

