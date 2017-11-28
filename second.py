from datetime import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook('Second.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)

worksheet.write('A1', 'First Name', bold)
worksheet.write('B1', 'Last name', bold)
worksheet.write('C1', 'Date of birth', bold)
worksheet.write('D1', 'City', bold)

data=[]

def getData():
	print("Enter the first name:")
	fname=str(raw_input())
	print("Enter the last name:")
	lname=str(raw_input())
	print("Enter the Date of Birth:")
	dob=str(raw_input())
	print("Enter the city:")
	city=str(raw_input())
	data.append([fname,lname,dob,city])

def addData():
	row = 1
	col = 0
	for fname, lname, dob,city in (data):
		date = datetime.strptime(dob, "%Y-%m-%d")
		worksheet.write(row,col,fname)
		worksheet.write(row,col + 1,lname)
		worksheet.write_datetime(row,col + 2,date,date_format)
		worksheet.write(row,col + 3,city)
		row += 1




for i in range(0,1):
	getData()
	
addData()
workbook.close()






