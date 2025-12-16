from fpdf import FPDF
from app.schemas import CleanedData

def generate_pdf(data: CleanedData, path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for k, v in data.dict().items():
        pdf.cell(200, 8, txt=f"{k}: {v}", ln=True)

    pdf.output(path)
