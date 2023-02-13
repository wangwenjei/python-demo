import pdfplumber
from openpyxl import Workbook

pdf = pdfplumber.open('aa.pdf')
page = pdf.pages[0]
print(page.extract_table())