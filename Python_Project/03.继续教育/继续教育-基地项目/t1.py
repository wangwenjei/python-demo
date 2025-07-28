import pdfplumber
from openpyxl import Workbook

pdf = pdfplumber.open('2022/aa.pdf')
page = pdf.pages[0]
print(page.extract_table())