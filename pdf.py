import PyPDF2

def extract(input_pdf, output_pdf, page):
    reader = PyPDF2.PdfFileReader("Firewall.pdf")
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addJS('app.alert("Startup");')
    with open('Firewall.pdf', 'wb') as f:
        pdf_writer.write(f)
        