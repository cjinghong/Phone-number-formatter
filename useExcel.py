import xlrd
import xlsxwriter
import os
import phonenumber

def readPhoneNumbers(workbook, sheetsAmt, hpColumn):
	# Stores the list of numbers
	number_list = []

	# Loops through the sheets
	for i in range(sheetsAmt):
		sheet = workbook.sheet_by_index(i)
		# Loops through every row, column hpColumn
		for j in range(sheet.nrows):
			value = str(sheet.cell_value(j, hpColumn))
			number_list.append(value.replace(" ", ""))

	return number_list

def printList(something):
	for stuffs in something:
		print(stuffs)

def writeToExcel(number_list, workbook_name):
	workbook = xlsxwriter.Workbook(workbook_name)
	worksheet = workbook.add_worksheet()

	for i in range(len(number_list)):
		worksheet.write(i, 0, number_list[i])

	workbook.close()


def main():
	# Sets the source and destination folder.
	sourceFolder = str(os.getcwd()) + "/Source/"
	destFolder = str(os.getcwd()) + "/Destination/"

	# User will get stuck here if file does not exist.
	while True:
		# Gets the excel file name from user
		file_name = input("Enter file name:\n")
		file_location = sourceFolder + file_name + ".xls"
		file_destination = destFolder + file_name + ".xls"

		if os.path.exists(file_location):
			break
		else :
			print ("Sorry the file does not exist.")
			print ("Enter again, or CTRL-C to exit.")
			continue

	# Read column from excel
	workbook = xlrd.open_workbook(file_location)

	# Gets number of sheets and the phone number column
	number_of_sheets = int(input("Enter number of sheets:\n"))
	phone_number_column = int(input("Enter the column number that contains the phone number:\n"))

	# readPhoneNumbers returns a list of phone numbers.
	phoneNumbers = readPhoneNumbers(workbook, number_of_sheets, phone_number_column)
	# Convert the phone number into the required format
	# Using the phonenumber module
	convertedPN = phonenumber.convertList(phoneNumbers)
	writeToExcel(convertedPN, file_destination)

if __name__ == "__main__":
	while True:
		print("Convert phone numbers")
		print("*********************")
		print("CTRL + C to exit.")
		main()