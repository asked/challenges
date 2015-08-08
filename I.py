import sys 
from fractions import gcd


	
	
def readNumber():
	Read = raw_input("Enter the top")
	TheComman = 1
	TheTop = 0
	Number = Read.split('+')
	top = [i.split('/')[0] for i in Number]
	TheBottom = [i.split('/')[1] for i in Number]
	for i in TheBottom:
		TheComman = eval(i) * TheComman 
	for i in top:
		TheTop = (eval (i)*TheComman) + TheTop
	print TheTop
	print '/'
	print TheComman
	

if __name__ == "__main__":
	
	readNumber()
