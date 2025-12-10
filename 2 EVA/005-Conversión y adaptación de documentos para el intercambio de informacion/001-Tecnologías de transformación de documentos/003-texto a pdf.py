#pip3 install fpdf --break-system-packages
from fpdf import FPDF

def texto_a_pdf(text, filename="salida.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.cell(0, 10, txt=line, ln=True)

    pdf.output(filename)

texto_a_pdf ("convertir.txt")
