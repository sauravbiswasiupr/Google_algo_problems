## Given a number find the number of 1s or the number of bits set in the 
## binary rep of the number

def countBits(n):
	if n == 0:
		return 0

	if n == 1:
		return 1

	count = 0
	while n > 0:
		n = n & (n-1)
		count = count + 1


	return count



if __name__ == '__main__':
	n = int(raw_input())
	print "One bits set are: ", countBits(n)