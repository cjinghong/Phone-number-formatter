import os.path
import sys

# Converts a list of phone numbers,
# and returns the converted list.
def convertList (file_list):
	# Stores the list of converted numbers
	new_list = []

	for number in file_list:
		number.strip()
		# Only stores number that starts with 01.....
		if (len(number) > 0):
			#if (number[0] == "'" and number[1] == "0"):
			if (number[0] == "0" and number[1] == "1"):
				if ("/" in number):
					numberslashes = number.split("/")
					for x in numberslashes:
						x = x.strip()
						newNum = x.replace("-", "")
						newNum = "6" + newNum
						new_list.append(newNum)
				else:
					newNum = number.replace("-", "")
					newNum = "6" + newNum
					newNum = newNum.strip()
					new_list.append(newNum)
			else:
				# Ignores the number if the number doesn't starts
				# with 01.....
				continue
	return new_list

# Reads phone numbers from a .txt document,
# returns a list of converted numbers.
def readNumFile(f):
	num_list = []

	for number in f:
		number.strip()
		print(number)
		# Only stores number that starts with 01.....
		if (number[0] == "0" and number[1] == "1"):
			print (number)
			if ("/" in number):
				print(number)

				numberslashes = number.split("/")
				for x in numberslashes:
					x = x.strip()
					newNum = x.replace("-", "")
					newNum = "6" + newNum
					num_list.append(newNum)
			else:
				newNum = number.replace("-", "")
				newNum = "6" + newNum
				newNum = newNum.strip()
				num_list.append(newNum)
		else:
			#(number == "\n" or number == "Contact No"):
			continue

	return num_list

# Takes a list and writes them into a .txt file.
def write_to_file(num_list, filename):

	newFile = open(filename, 'w')

	for x in num_list:
		if x != '6':
			newFile.write(x+"\n")

# Takes 2 arguments,
# fromFile: the .txt file that contains phone numbers
# toFile: name of file to write to
def convertFile(fromFile, toFile):
	# Checks if the destination file already exist.
	if (os.path.isfile(toFile)):
		# Promt user if they want to overwrite the file IF IT EXISTS.
		while True:
			overwrite = input("File already exists. Overwrite? (Y/N)")
			if (overwrite != "Y" and overwrite != "N"):
				print("Invalid input. Please try again.")
			# If user chose to overwrite the file
			elif (overwrite == "Y"):
				f = open(fromFile,"r")
				nf = open(toFile, "w")
				filelist = readNumFile(f)
				for x in filelist:
					if x != '6':
						nf.write(x+"\n")
			else:
				input("Hit enter to exit.")
				sys.exit()
	else:
		f = open(fromFile,"r")
		nf = open(toFile, "w")
		filelist = readNumFile(f)

		for x in filelist:
			if x != '6':
				nf.write(x+"\n")

def main():
	readFiles = input("Enter the read file names, separated by commas:\n")
	destFiles = input("Enter the save file names, separated by commas:\n")
	readFiles = readFiles.strip()
	destFiles = destFiles.strip()
	read_file_collections = readFiles.split(",")
	dest_file_collections = destFiles.split(",")

	for i in range(len(read_file_collections)):
		convertFile(read_file_collections[i], dest_file_collections[i])
		input("Done!\nPress anykey to continue, CTRL+C to exit.")

if __name__ == "__main__":
	main()