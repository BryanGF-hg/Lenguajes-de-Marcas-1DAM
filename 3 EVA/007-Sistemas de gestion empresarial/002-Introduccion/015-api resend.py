import os
from resend import Resend

# Cargar API key
api_key = os.environ.get("RESEND_API_KEY")

if not api_key:
    raise ValueError("RESEND_API_KEY no está configurada. Ejecuta: source ~/.bashrc")

# Inicializar cliente Resend
resend = Resend(api_key)

try:
    # Enviar email usando la API de Resend (más simple)
    response = resend.Emails.send({
        "from": "Acme <onboarding@resend.dev>",  # Email de prueba de Resend
        "to": ["tsarhiro@protonmail.com"],
        "subject": "Prueba desde Python con Resend API",
        "html": "<strong>Hola, esto es una prueba desde Python usando Resend API!</strong>",
        "text": "Hola, esto es una prueba desde Python usando Resend API!"
    })
    
    print(f"✅ Email enviado! ID: {response['id']}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Instala la librería Resend:")
    print("pip install resend")
