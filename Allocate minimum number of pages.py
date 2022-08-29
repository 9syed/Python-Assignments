def minpages(arr, x, y, z):
	students = 1
	curr_sum = 0

	for i in range(x):
		if (arr[i] > z):
			return False
		if (curr_sum + arr[i] > z):
			students += 1
			curr_sum = arr[i]

			if (students > y):
				return False

		else:
			curr_sum += arr[i]

	return True

def numberofpages(arr, x, y):

	sum = 0
	if (x < y):
		return -1
	for i in range(x):
		sum += arr[i]

	start, end = 0, sum
	result = 10**9

	while (start <= end):
		mid = (start + end) // 2
		if (minpages(arr, x, y, mid)):
			result = mid
			end = mid - 1

		else:
			start = mid + 1
	return result

arr = [12, 34, 67, 90]
x = len(arr)
y = 2

print(numberofpages(arr, x, y))