t = int(raw_input())
def removepositive(x):
	if x<=0:
		return True
	else:
		return False
for c in range (t):
	nk = raw_input()
	nklist = nk.split()
	#total students
	students = int(nklist[0])
	#min students present at t 1 for 'no' result/class NOT cancelled
	minstudents = int(nklist[1])
	times = raw_input()
    #list of arrival times, converted to ints
	timelist = times.split()
	tlints = [int(x) for x in timelist]
    #filter all arrival times except students who were on time (at or before t=0)
	#removes all list entries in second (list) argument for which the first (function) argument returns FALSE
	present = filter(removepositive, tlints)
	if len(present) >= minstudents:
        #class NOT cancelled
		print "NO"
	else:
        #class IS cancelled
		print "YES"
#this one is confusing as FUCK because the initial test case succeeds, even if you were assuming that negative time = late, but actually negative time = early
#would probably have failed on later test cases