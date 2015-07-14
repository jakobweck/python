import itertools
initstring = raw_input()
target = int(raw_input())
mainlist = initstring.split()
resultlist =[]
difflist=[]
for i in list(itertools.combinations(mainlist,3)):
	numcomb = map(int,i)
	isum = sum(numcomb)
	resultlist.append(isum)
for i in resultlist:
	diff = i - target
	difflist.append(diff)
if 0 in difflist:
	print target
else: 
	index = difflist.index(min(difflist))
	print resultlist[index]