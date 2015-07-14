test_cases = int(raw_input())
cases_tested = 0
def find_height(n):
	height = 1
	for i in range(1,n+1):
		if i%2 == 0:
			height +=1
		else:
			height *=2
	return height 
while cases_tested < test_cases:
    cycles = int(raw_input())
    final_height = find_height(cycles)
    print final_height
    cases_tested+=1