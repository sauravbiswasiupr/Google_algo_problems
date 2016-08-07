## Given an array of intervals (start, end) delete all the intervals which are subsets of an intervals
def isSubset(interval1, interval2):
	if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
		return True

	else:
		return False

def deleteSubIntervals(intervals):
	if intervals == None:
		return None

	n = len(intervals)
	if n == 0:
		return []

	if n == 1:
		return intervals

	intervals.sort(key=lambda x:x[0])
	start = intervals[0]

	results = [start]

	for interval in intervals[1:]:
		if isSubset(start, interval):
			continue

		elif isSubset(interval, start):
			start = interval
			results.pop()

		else:
			results.append(interval)
			start = interval


	return results


if __name__ == '__main__':
	l = raw_input().split(" ")
	def inline_split(l):
		i,j = l.split(",")
		i = int(i)
		j = int(j)
		return (i, j)


	list = map(inline_split, l)
	print "The new list of intervals is: ", deleteSubIntervals(list)



