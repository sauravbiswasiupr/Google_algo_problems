## Given a list of integers, find highest value obtainable by concatenating these
## together

def findHighestValue(l):
	if l == None or len(l) == 0:
		return None

	str_list = map(lambda x: str(x), l)
	str_list.sort(key = lambda x: (x[0], x[-1]), reverse=True)

	return reduce(lambda x, y: x + y, str_list)

if __name__ == '__main__':
	nums = map(lambda x: int(x), raw_input().split(" "))
	print "Greatest number possible: ", findHighestValue(nums)