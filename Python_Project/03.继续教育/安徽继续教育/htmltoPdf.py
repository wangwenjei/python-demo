import pdfkit
import wkhtmltopdf
html_file = 'input.html'


options = {
    'page-size': 'A4',
    'encoding': 'UTF-8',
    'enable-local-file-access': None
}

pdfkit.from_file(html_file, 'output.pdf', options=options)


"""
arch -arm64 brew install wkhtmltopdf

brew install --cask wkhtmltopdf

 pip install pdfkit
(python-demo) JasondeMacBook-Pro:安徽继续教育 jason$ pip install wkhtmltopdf
Requirement already satisfied: wkhtmltopdf in /Users/jason/python-demo/python-demo/lib/python3.8/site-packages (0.2)


"""