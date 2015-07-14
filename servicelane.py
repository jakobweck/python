#string containing length of freeway and num of cases
nt = raw_input()
#string containing widths of side-lane segments
widths = raw_input()
#split strings into lists
ntlist = nt.split()
widthlist = widths.split()
#assign freeway length and number of cases to variables
fwlen = int(ntlist[0])
cases = int(ntlist[1])
#iterate for all cases
for c in range (0, cases):
	#string containing segments where he enters/exits the side lane
	ij = raw_input()
	#split into list and assign to variables
	ijlist = ij.split()
	i = int(ijlist[0])
	j = int(ijlist[1])
	#use to create list containing widths of segments passed through
	visitedlist = widthlist[i:j+1]
	#find narrowest visited segment (equivalent to narrowest possible vehicle)
	narrow = min(visitedlist)
	print narrow 