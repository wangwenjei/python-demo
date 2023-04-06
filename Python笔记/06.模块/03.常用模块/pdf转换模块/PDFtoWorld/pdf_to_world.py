from pdf2docx import Converter

"""
    pip install pdf2docx==0.5.6
"""

pdf_file = './20230404.pdf'
docx_file = './20230404.docx'
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
