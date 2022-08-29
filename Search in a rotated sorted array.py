def search(arr, x, y, key):
	if x > y:
		return -1

	mid = (x + y) // 2
	if arr[mid] == key:
		return mid

	if arr[x] <= arr[mid]:

		if key >= arr[x] and key <= arr[mid]:
			return search(arr, x, mid-1, key)
		return search(arr, mid + 1, y, key)

	if key >= arr[mid] and key <= arr[y]:
		return search(arr, mid + 1, y, key)
	return search(arr, x, mid-1, key)


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
i = search(arr, 0, len(arr)-1, key)
if i != -1:
	print("Found at index %d" % i)
else:
	print("Not found")