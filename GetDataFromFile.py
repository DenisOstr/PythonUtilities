""" 
This program performs the functions of retrieving data from a file
and formatting it into another format:

	{ format }: 'Word/Word'
	{ format }: 'Name of University + delimeter: (-)'

Developed by Denis Ostrovsky
"""


def getCitiesData():
	""" 
	This function gets the data from the file and formats it in this format:

		{ format }: 'City/Country'
	"""

	print('(Info): Select the name of the file you will work with.')
	print('(Notice): Example the file name `test.txt`.')
	fileName = input('> ')

	if fileName == 'exit':
		exit()

	try:
		fopen = open(fileName, 'r')
	except:
		print('(Error): This file was not found!')
		exit()

	dataList = []

	for items in fopen:
		items = items.split()

		dataList.append(data)
		data = items[0] + '/' + items[1]
		dataList.append(data)

	return dataList


def getUniversitiesData():
	""" 
	This function gets the data from the file and formats it in this format:

		{ format }: 'Name of University + delimeter: (-)'
	"""

	print('(Info): Select the name of the file you will work with.')
	print('(Notice): Example the file name `test.txt`.')
	fileName = input('> ')

	if fileName == 'exit':
		exit()

	try:
		fopen = open(fileName, 'r')
	except:
		print('(Error): This file was not found!')
		exit()

	resList = []

	for items in fopen:
		items = items.rstrip()

		fPos = items.find(',')
		sPos = items.find(',', items.find(',') + 1)

		resItems = items[fPos + 1:sPos]
		resItems = resItems.rstrip()

		if resItems.startswith('"'):
			resItems = items[fPos + 2:sPos]
			resItems = resItems.rstrip()

		if resItems.endswith('"'):
			resItems = items[fPos + 2:sPos - 1]
			resItems = resItems.rstrip()

		resItems = resItems.split()

		delimeter = '-'
		resItems = delimeter.join(resItems)

		resList.append(resItems)

	return resList


def postData():
	""" 
	This function post the data to the file in the new format:

		{ format }: 'City/Country'
		{ format }: 'Name of University + delimeter: (-)'
	"""

	print('(Info): Select the name of the file in which you will save the data.')
	print('(Notice): Example the file name `test.txt`.')
	fileName = input('> ')

	if fileName == 'exit':
		exit()

	try:
		fopen = open(fileName, 'w+')
	except:
		print('(Error): This file was not found!')
		exit()

	print('(Info): Select the function `1` to save similarity data:')
	print('(Notice): Example. `Word Word`, Formatting view. `Word/Word`')
	print('(Info): Select the function `2` to save similarity data:')
	print('(Notice): Example. `Word, Word ..., Word`, Formatting view. `, Word-Word-Word,`')
	
	postFuncSelect = input('> ')

	itemsSave = ''

	if postFuncSelect == '1':
		gcd = getCitiesData()

		for items in gcd:
			itemsSave += items + '\n'
	elif postFuncSelect == '2':
		gud = getUniversitiesData()

		for items in gud:
			itemsSave += items + '\n'

	fopen.write(itemsSave)


if __name__ == '__main__':
	print('(Info): Select the `get` function to get data from a file and process it.')
	print('(Info): Select the `1` function to work with Cities Data.')
	print('(Info): Select the `2` function to work with Universities Data.')
	print('(Info): Select the `post` function to post data to a another file.')
	
	userInput = input('> ')
	funcNum = input('> ')

	if userInput == 'get':
		if funcNum == '1':
			getCitiesData()
		elif funcNum == '2':
			getUniversitiesData()
	elif userInput == 'post':
		postData()
	elif userInput == 'exit':
		exit()
	else:
		print('(Error): This is error input!')
	