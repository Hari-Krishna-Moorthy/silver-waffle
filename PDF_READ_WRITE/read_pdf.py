from PyPDF2 import PdfFileReader

file_path = 'file.pdf'

pdf = PdfFileReader(file_path)


# print("No of Pages :", pdf.getNumPages())
# print("Document Info : ", pdf.documentInfo)


# Get First page text

for page_number in range(pdf.getNumPages()):
	page = pdf.getPage(page_number)
	page_content = page.extractText()
	print(page_content)

