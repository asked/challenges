'''Fractions are the bane of existence for many elementary and middle-schoolers.
 They're sort-of hard to get your head around (though thinking of them as pizza slices turned out to be very helpful for me), 
 but even worse is that they're so hard to calculate with! Even adding them together is no picknick.

Take, for instance, the two fractions 1/6 and 3/10. 
If they had the same denominator, you could simply add the numerators together, but since they have different denominators, you can't do that.
 First, you have to make the denominators equal. The easiest way to do that is to use cross-multiplication to make both denominators 60 (i.e. the original denominators multiplied together, 6 * 10).
 Then the two fractions becomes 10/60 and 18/60, and you can then add those two together to get 28/60.

(if you were a bit more clever, you might have noticed that the lowest common denominator of those fractions is actually 30, not 60, but it doesn't really make much difference).

You might think you're done here, but you're not! 28/60 has not been reduced yet, those two numbers have factors in common!
 The greatest common divisor of both is 4, so we divide both numerator and denominator with 4 to get 7/15, which is the real answer. '''

import sys 
from fractions import gcd


	
	
def readNumber():
	Read = raw_input("Enter the top")
	TheComman = 1
	TheTop = 0
	Number = Read.split('+')
	print Number
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
