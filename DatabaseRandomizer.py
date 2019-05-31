""" 
Randomizer for database. Randomly creates records for databases.

This program performs the functions of generating a csv file
for further import into the PostgreSQL database management system.

Developed by Denis Ostrovsky
"""

import random
import string


class StudentList():
	"""This class handles functions for populating databases with information."""

	def getDataFile(self):
		""" 
		This function performs the main task of forming the final csv file.
		"""

		csvFile = open('studentList.csv', 'w+')

		''' Variables '''
		insNum = self.insuranceNumber()
		listInsNum = str(insNum)

		lsName = self.lastName()

		fsName = self.firstName()

		birthYear = self.yearOfBirth()

		birthCity = self.cityOfBirth()

		universities = self.university()

		idNum = self.id()

		stndls = ''

		''' Loop for get the data and forming the final result '''
		for itemsId, itemsNum, itemsLN, itemsFN, itemsYB, itemsCB, ItemsU in zip(
										idNum,
										insNum, 
										lsName, 
										fsName, 
										birthYear, 
										birthCity,
										universities
										):
			stndls += itemsId + ',' + itemsNum + ',' + itemsLN + ',' + itemsFN + ',' + itemsYB + ',' + itemsCB + ',' + ItemsU + '\n'

		csvFile.write(stndls)


	def id(self):
		idNumber = []

		for i in range(1, 1001):
			idNumber.append(str(i))

		return idNumber

		
	def insuranceNumber(self):
		""" 
		This function performs the task of generating the Insurance Number.
		"""

		startDigit = 1000000000
		endDigit = 9999999999

		resInsuranceNumber = []

		for i in range(1000):
			insNum = random.randint(startDigit, endDigit)

			resInsuranceNumber.append(str(insNum))

		return resInsuranceNumber

	def lastName(self):
		""" 
		This function performs the task of get the data about all surname
		and formating this data to database (csv) view.
		"""

		''' 
		{ Stupid data processing }: transferring data to a list, 
		and then repeating the same action using a loop and another list!
		'''

		try:
			fopen = open('listLastNames.txt', 'r')
			allLNames = fopen.read()
			fopen.close()
		except:
			print('(Error): This file was not found!')
			exit()

		allLNames = allLNames.split()

		listLNames = []
		randLNames = []

		for name in allLNames:
			listLNames.append(name)

		for lnames in listLNames:
			randName = random.choice(listLNames)

			randLNames.append(randName)

		return randLNames
			

	def firstName(self):
		""" 
		This function performs the task of get the data about all first name
		and formating this data to database (csv) view.
		"""

		''' 
		{ Stupid data processing }: transferring data to a list, 
		and then repeating the same action using a loop and another list!
		'''

		try:
			fopen = open('listFirstNames.txt', 'r')
			allFNames = fopen.read()
			fopen.close()
		except:
			print('(Error): This file was not found!')
			exit()

		allFNames = allFNames.split()

		listFNames = []
		randFNames = []

		for name in allFNames:
			listFNames.append(name)

		for fnames in listFNames:
			randName = random.choice(listFNames)

			randFNames.append(randName)

		return randFNames


	def yearOfBirth(self):
		""" 
		This function performs the task of generating the year of birth.
		"""

		randListYears = []

		for years in range(1000):
			randYears = random.randint(1971, 1990)
			randListYears.append(str(randYears))

		return randListYears


	def cityOfBirth(self):
		""" 
		This function performs the task of get the data about all cities of birth
		and formating this data to database (csv) view.
		"""

		''' 
		{ Stupid data processing }: transferring data to a list, 
		and then repeating the same action using a loop and another list! 
		'''

		try:
			fopen = open('listCities.txt', 'r')
			allCities = fopen.read()
			fopen.close()
		except:
			print('(Error): This file was not found!')
			exit()

		allCities = allCities.split()

		listCities = []
		randListCities = []

		for name in allCities:
			listCities.append(name)

		for cnames in listCities:
			randCityName = random.choice(listCities)

			randListCities.append(randCityName)

		return randListCities


	def university(self):
		""" 
		This function performs the task of get the data about all university
		and formating this data to database (csv) view.
		"""

		''' 
		{ Stupid data processing }: transferring data to a list, 
		and then repeating the same action using a loop and another list! 
		'''

		try:
			fopen = open('listUniversities.txt', 'r')
			allUniversities = fopen.read()
			fopen.close()
		except:
			print('(Error): This file was not found!')
			exit()

		allUniversities = allUniversities.split()

		listUniversities = []
		randListUniversities = []

		for name in allUniversities:
			delimeter = '-'

			name = name.split(delimeter)

			listUniversities.append(name)

		for cnames in listUniversities:
			randUniversitiesName = random.choice(listUniversities)

			delimeter = ' '

			randUniversitiesName = delimeter.join(randUniversitiesName)

			randListUniversities.append(randUniversitiesName)

		return randListUniversities


if __name__ == '__main__':
	sl = StudentList()
	sl.getDataFile()