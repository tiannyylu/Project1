import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv


def getData(file):
	"""The function extracts a file from your computer

	and returns a list of dictionaries in which the keys are the headers
	and the values are the rows under the headers.
	"""
	inFile = open(file, "r")
	lines = inFile.readlines()
	myDicts = []
	for line in lines[1:]:
		d = dict()
		item = line.split(",")
		first = item[0]
		last = item[1]
		email = item[2]
		c = item[3]
		dob = item[4]

		d['First'] = first
		d['Last'] = last
		d['Email'] = email
		d['Class'] = c
		d['DOB'] = dob

		myDicts.append(d)
	inFile.close()
	return myDicts
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	pass

def mySort(data,col):
	"""The function returns the data in the list of dictionaries in a sorted order based on the specifc input value

	data - list of dictionaries
	col - the value the dictionaries are sorted on
	"""
	sorted_d = sorted(data, key = lambda k: k[col])
	sorted_first = sorted_d[0]
	return sorted_first['First'] + ' ' + sorted_first['Last']
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	pass


def classSizes(data):
	"""The function returns a list of tuples from largest class to smallest class

	data - list of dictionaries
	"""
	class_dict = {}
	for d in data:
		if d['Class'] not in class_dict:
			class_dict[d['Class']] = 0
		class_dict[d['Class']] += 1

	return sorted(class_dict.items(), key = lambda tup: tup[1], reverse = True)
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	pass


def findMonth(a):
	"""The function finds and returns the most common birth month."""
	month_dict = {}
	for d in a:
		birth_dates = d['DOB']
		lst_dob = birth_dates.split('/')
		month = lst_dob[0]
		if month not in month_dict:
			month_dict[month] = 0
		month_dict[month] += 1
	sorted_months = sorted(month_dict.items(), key = lambda tup: tup[1], reverse = True)
	return int(sorted_months[0][0])
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	pass

def mySortPrint(a,col,fileName):
	"""The function sorts the list of dictionaries based on a value and writes the sorted list into a csv file

	a - list of dictionaries
	col - value the list of dictionaries is sorted on
	fileName - the output file name
	"""
	outfile = open(fileName, 'w')
	sorted_d = sorted(a, key = lambda k: k[col])
	for student_info in sorted_d:
		firstName = student_info['First']
		lastName = student_info['Last']
		email = student_info['Email']
		outfile.write('{},{},{}\n'.format(firstName, lastName, email))

	outfile.close()
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
	"""The function finds the age of the students using their DOB and returns the average age."""
	today = date.today()
	ageLst = []
	for person in a:
		dob = person['DOB']
		dobLst = dob.split('/')
		month = int(dobLst[0])
		day = int(dobLst[1])
		year = int(dobLst[2])
		born = date(year, month, day)
		age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		ageLst.append(age)
	avgAge = round(sum(ageLst)/len(ageLst))
	return avgAge
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
