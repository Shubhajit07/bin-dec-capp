from os import system, name 
from time import sleep
from colorama import init
from termcolor import colored
init()

def clear():
    if name == 'nt': 
    	_ = system('cls') 

    else: 
    	 _ = system('clear') 

#Defining dialog function
def dialog(tool):
	choice = input(colored("\n\nEnter 0 to exit\n1 to go to main menu\n2 To use this tool again: ","cyan"))
	if choice=='0':
		exit()
	elif choice=='1':
		clear()
		main()
	elif choice=='2' or choice=="":
		clear()
		if tool=="dtb":
			sleep(0.1)
			dtb()
		elif tool=="btd":
			sleep(0.1)
			btd()
		else:
			main()
		
	else:
		clear()
		print(colored("\nWrong choice.\nSending to to main menu in 3 seconds","red"))
		sleep(3)
		clear()
		main()



def main():
	clear()
	print(colored(
	"""
	|------------Tools list-------------|
	|   1) Decimal to Binary converter  |
	|   2) Binary to Decimal converter  |
	|   3) Exit from this tool  	    |
	|   Enter 1 or 2 to select the tool |
	|-----------------------------------|
		
	""","green")
	)
	
	choice = input(colored("Your choice (1/2/3): ","cyan"))
	if choice == '1':
		dtb()
	elif choice == '2':
		btd()
	elif choice=='3':
		exit()
	else:
		print(colored("\nWrong choice","red"))
		sleep(0.5)
		clear()
		main()

#Defining Decimal to Binary converter function
def dtb():
	clear()
	print(colored("""
	--------------------------------------------
		Decimal to Binary converter
	--------------------------------------------
	""","green"))
	decimal = None
	dec_input = None
	
	#Getting Integer Input
	while decimal==None:
		#Handling Value Error
		try:
			user_in = input(colored("Enter a decimal value: ","cyan"))
			if user_in=="exit":
				exit()
			elif user_in=="main":
				main()
			else:
				dec_input = int(user_in)
		except ValueError:
			print(colored("Please enter an integer value\n","yellow"))
			sleep(0.1)
		if dec_input!=None:
			if dec_input == 0:
				print(colored("Input value can't be zero!\n","yellow"))
				sleep(0.1)
			elif dec_input<0:
				print(colored("Input value can't be negative\n","yellow"))
				sleep(0.1)
			else:
				decimal=dec_input
				
	
	#Converting Decimal To Binary
	binary=[]
	while decimal != 0:
		r=decimal%2
		decimal=(decimal-r)/2
		binary.insert(0,r)
	sleep(0.1)
	print(colored("Binary value is: ","green"), end='')
	for n in binary:
		print(colored(int(n),"green"),end='')
	dialog("dtb")

#Defining Binary to Decimal converter function
def btd():
	clear()
	print(colored("""
	--------------------------------------------
		Binary to Decimal converter
	--------------------------------------------
	""","green"))
	binary=[]
	loop=True
	while loop:
		raw_in=input(colored("Please enter a binary value: ","cyan"))
		rec_in=raw_in.replace(" ","")
		if rec_in=="exit":
			exit()
		elif rec_in=="main":
			main()
		try:
			for d in rec_in:
				val=int(d)
				if val==0 or val==1:
					binary.insert(0,val)
					loop = False
				else:
					raise ValueError("Not a binary code, binary code is combination of zero's and one's")
		except ValueError:
				print(colored("Not a binary code","yellow"))
				sleep(0.1)
				loop = True
				
	decimal=0
	power=0
	for b in binary:
		if b==1:
			b=2
		else:
			b=0
		if b==2:
			decimal+=b**power
		power+=1	
	print(colored(f"Decimal value is: {decimal}","green"))
	dialog("btd")

if __name__ =='__main__':
	main()
