import PyPDF2
from tabula.io import read_pdf
import pdfplumber
import pandas as pd
  
pdf_path = '/Users/divakar/Desktop/TheCodeWork/pdf_scrapper/srulibruck-attachments/May_2022_RT.pdf'

def extract_information1(pdf_path):
	try:
		data = {}
		pdf = open(pdf_path, 'rb')
		pdf_reader = PyPDF2.PdfFileReader(pdf)
		if pdf_reader.numPages == 0:
			return False, {}
		page_one = pdf_reader.getPage(0)
		page_one_text = page_one.extractText().split('\n')
		# Business name...
		data.update({'business_name': page_one_text[3]})
		#Beginning Balance Date
		beginning_balance = page_one_text[15].split()
		beginning_balance_date = beginning_balance[3] + ' ' + beginning_balance[4] + ' ' + beginning_balance[5]
		data.update({'beginning_balance_date': beginning_balance_date})
		# Beginning balance
		data.update({'beginning_balance': beginning_balance[6]})
		# Deposit Total
		Deposit_total_str = page_one_text[16].split()[4].split('W')[0]
		data.update({'Deposit_total': Deposit_total_str}) 
		# Ending Balance Date
		ending_balance = page_one_text[19].split()
		ending_balance_date = ending_balance[3] + ' ' + ending_balance[4] + ' ' + ending_balance[5]
		data.update({'ending_balance_date': ending_balance_date})
		# Ending Balance..
		ending_balance = ending_balance[6] 
		if '#' in ending_balance:
			ending_balance = ending_balance[:-1]
		data.update({'ending_balance': ending_balance})
		# ## Extract info from page no 5...
		# page_five = pdf_reader.getPage(4)
		# page_five_text = page_five.extractText().split('Daily ledger balances')
		# #Daily ledger balances
		# print(page_five_text[-1])
		# table_pdf = read_pdf(pdf, pages = "all", multiple_tables=True, guess=True)
		# for table in table_pdf:
		# 	print(table)
		# 	print("----------------&&&&&&&&&---------------------------")
		print(data)
		pdf.close()
	except Exception as e:
		print(e)

def extract_information2(pdf_path):
	try:
		data = {}
		pdf = open(pdf_path, 'rb')
		pdf = pdfplumber.open(pdf_path)
		page = pdf.pages[0]
		text = page.extract_text()
		print("--------------------------")
		print(text)
		# pdf_reader = PyPDF2.PdfFileReader(pdf)
		# if pdf_reader.numPages == 0:
		# 	return False, {}
		# page_one = pdf_reader.getPage(0)
		# page_one_text = page_one.extractText().split('\n')
		# data.update({'business_name': page_one_text[3]})
		# print(page_one.extractText())
		# import pdb; pdb.set_trace()
		#text.split('Beginning Balance')[1].split('Enclosures')[0]
		with open('text2.txt', 'w', encoding="utf-8") as f:
			f.write(text)
		# import pdb; pdb.set_trace()
	except Exception as err:
		print("err", err)


if __name__ == "__main__":
	# extract_information1(pdf_path)
	extract_information2(pdf_path)



# pdf = pdfplumber.open('/Users/divakar/Desktop/TheCodeWork/pdf_scrapper/srulibruck-attachments/04-2022 - 2022-07-06T151714.346.pdf')
# page = pdf.pages[0]
# text = page.extract_text()
# print("--------------------------")
# print(text)