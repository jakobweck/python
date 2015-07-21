#implementation of euclid's algorithm for finding gcd of 2 numbers
m = int(raw_input())
n = int(raw_input())
# m is the dividend, n is the divisor
#passing the important variables as arguments from the last iteration
#ensures that they don't get reset to their initial values
#when the function loops
#you can't just set local variables equal to the input variables
def main(dividend,divisor):
	#init local vars equal to args
	divid = dividend
	divis = divisor
	# r is the remainder after the two args are divided
	r = divid % divis
	#if m divides n evenly and r is zero, n must be the gcd
	if r == 0:
		print divis
	else:
	# otherwise, the divisor becomes the new dividend
	# r becomes the new divisor
		divid = divis 
		divis = r
	#repeat the function with these new values
		main(divid, divis)
#run main loop, starting with input values
main(m,n)