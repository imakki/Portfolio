###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
	if day < 3:0
		return year, month, day+1
	if month == 12:
		return year + 1 , 1, 1
	else:
		return year , month + 1, 1

print nextDay(1999, 12, 30) #=> (2000, 1, 1)
print nextDay(2013, 1, 30) #=> (2013, 2, 1)
print nextDay(2012, 12, 30) #=> (2013, 1, 1)
print nextDay(1997, 5, 1)
print nextDay(2016, 6, 30)
print nextDay(2012, 1, 1)
