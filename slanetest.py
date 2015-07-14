#list containing length of freeway and num of cases
nt = raw_input().split
#list containing widths of side-lane segments
widths = raw_input().split
#assign freeway length and number of cases to variables
fwlen = int(nt[0])
cases = int(nt[1])
#iterate for all cases
for c in range (cases):
	#string containing segments where he enters/exits the side lane
	ij = raw_input().split
	# assign to variables
	i = int(ij[0])
	j = int(ij[1])
	#use to create list containing widths of segments passed through
	visitedlist = width[i:j+1]
	#find narrowest visited segment (equivalent to narrowest possible vehicle)
	narrow = min(visitedlist)
	print narrow 