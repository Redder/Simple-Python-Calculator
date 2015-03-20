import sys
import os
import time
def welcome():
	os.system('cls') #os.system('clear') If on linux
	print('================================')
	print('  Welcome to a Basic Calculator ')
	print('      Operations Supported:')
	print('             Addition')
	print('            Subtraction')
	print('          Multiplication')
	print('              Division')
	print('================================')
	#Prints choices
	print('Which Operation do you want to perform?')
	print('1: Addition')
	print('2: Subtraction')
	print('3: Multiplication')
	print('4: Division')
	
choice = 'retry'
#Print Welcome Screen
while  True:
	if choice == 'retry':
		welcome()
	try:
		choice = int(raw_input('Please Choose Operation: '))
		while choice == 1:
			def add(num1,num2):
				num3 = num1 + num2
				return num3
			os.system('cls')
			print('Addition')
			print('================================')
			try:
				num1 = int(raw_input('Please enter the first number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num1 = 0
				raw_input('')
			try:
				num2 = int(raw_input('Please enter the Second number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num2 = 0
				raw_input('')
			ans = add(num1,num2)
			print(str(num1) + ' + ' + str(num2) + ' = ' + str(ans))
			print('================================')
			raw_input('')
			os.system('cls')
			print('Do you want to continue with Addition?')
			print('1: Yes')
			print('2: No')
			try:
				answer = int(raw_input(''))
				if answer == 2:
					choice = 'retry'
					pass
			except ValueError:
				print('Input was Invalid! Please input a number!')
				raw_input('')
				
		
		while choice == 2:
			def sub(num1,num2):
				num3 = num1 - num2
				return num3
			os.system('cls')
			print('Subtraction')
			print('================================')
			try:
				num1 = int(raw_input('Please enter the first number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num1 = 0
				raw_input('')
			try:
				num2 = int(raw_input('Please enter the Second number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num2 = 0
				raw_input('')
			ans = sub(num1,num2)
			print(str(num1) + ' - ' + str(num2) + ' = ' + str(ans))
			print('================================')
			raw_input('')
			os.system('cls')
			print('Do you want to continue with Subtraction?')
			print('1: Yes')
			print('2: No')
			try:
				answer = int(raw_input(''))
				if answer == 2:
					choice = 'retry'
					pass
			except ValueError:
				print('Input was Invalid! Please input a number!')
				raw_input('')
		while choice == 3:
			def multi(num1,num2):
				num3 = num1*num2
				return num3
			os.system('cls')
			print('Multiplication')
			print('================================')
			try:
				num1 = int(raw_input('Please enter the first number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num1 = 0
				raw_input('')
			try:
				num2 = int(raw_input('Please enter the Second number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num2 = 0
				raw_input('')
			ans = multi(num1,num2)
			print(str(num1) + ' * ' + str(num2) + ' = ' + str(ans))
			print('================================')
			raw_input('')
			os.system('cls')
			print('Do you want to continue with Multiplication?')
			print('1: Yes')
			print('2: No')
			try:
				answer = int(raw_input(''))
				if answer == 2:
					choice = 'retry'
					pass
			except ValueError:
				print('Input was Invalid! Please input a number!')
				raw_input('')

		while choice == 4:
			def div(num1,num2):
				num3 = num1 / num2
				return num3
			os.system('cls')
			print('Division(No Remainders)')
			print('================================')
			try:
				num1 = int(raw_input('Please enter the first number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num1 = 0
				raw_input('')
			try:
				num2 = int(raw_input('Please enter the Second number: '))
			except ValueError:
				print('Input was Invalid! Please input a number!')
				num2 = 0
				raw_input('')
			ans = div(num1,num2)
			print(str(num1) + ' / ' + str(num2) + ' = ' + str(ans))
			print('================================')
			raw_input('')
			os.system('cls')
			print('Do you want to continue with Division?')
			print('1: Yes')
			print('2: No')
			try:
				answer = int(raw_input(''))
				if answer == 2:
					choice = 'retry'
					pass
			except ValueError:
				print('Input was Invalid! Please input a number!')
				raw_input('')
	except ValueError:
		print('Input was Invalid! Please input a number!')
		raw_input('')

	#sys.exit
		pass


print(choice)
