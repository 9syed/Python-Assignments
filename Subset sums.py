def subsetsums(arr, x, y, sum=1):

	if x > y:
		print(sum, end=" ")
		return

	subsetsums(arr, x + 1, y, sum + arr[x])
	subsetsums(arr, x + 1, y, sum)

arr = [2, 4, 5]
n = len(arr)
subsetsums(arr, 0, n - 1)