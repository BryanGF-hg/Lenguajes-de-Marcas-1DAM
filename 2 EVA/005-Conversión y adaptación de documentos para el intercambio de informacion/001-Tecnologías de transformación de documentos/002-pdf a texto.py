#pip3 install pypdf --break-system-packages
from pypdf import PdfReader

lector = PdfReader("perfect.pdf")
texto = ""

for pagina in lector.pages:
 texto += pagina.extract_text() + "\n"
 
print(texto)
