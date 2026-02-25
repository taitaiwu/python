def parting(nums: list[int], left: int, right: int) -> int: 
	i = left
	j = right

	while (i < j):
		while ((i < j) and (nums[j] >= nums[left])):
			j -= 1
		
		while ((i < j) and (nums[i] <= nums[left])):
			i += 1

		if (i < j):
			nums[i], nums[j] = nums[j], nums[i]

	nums[i], nums[left] = nums[left], nums[i]
	return i

def quick_sort(nums: list[int], left: int, right: int): 
	while (left < right):
		index = parting(nums, left, right)

		if (index - left < right - index):
			quick_sort(nums, left, index-1)
			left = index + 1

		else:
			quick_sort(nums, index+1, right)
			right = index - 1

def insert_sort(nums: list[int]):
	for i in range(1, len(nums)):
		num = nums[i]
		j = i - 1

		while ((j >= 0) and (nums[j] > num)):
			nums[j+1] = nums[j]
			j -= 1

		nums[j+1] = num

print("Homework1 - Quick Sort & Insertion Sort")
print("---------------------------------------")

while (True):
	try:
		print("Select one of the following modes.")
		print("(1) Quick Sort")
		print("(2) Insertion Sort")
		print("(3) Exit")
		user = int(input("Please enter a integer between 1 to 3 : "))

		if (user == 1):
			print("\nSelect one of the following file.")
			print("(1) test1.txt")
			print("(2) test1_200.txt")
			print("(3) test1_500.txt")
			file = input("Please enter a integer between 1 to 3 : ")

			if file == "1":
				f = open("test1.txt")
			elif file == "2":
				f = open("test1_200.txt")
			elif file == "3":
				f = open("test1_500.txt")
			else:
				print("\nInput Error!")
				print("---------------------------------------\n")
				continue

			size = int(f.readline().replace("\n", ""))
			nums = f.readline().replace("\n", "").split()
			nums = [float(i) for i in nums]
			origin_nums = nums.copy()
			f.close()

			quick_sort(nums, 0, size-1)

			print("\n----Quick Sort-------------------------")
			print("(1) The number of all numbers :", len(nums), "\n")
			print("(2) Maximum number :", nums[-1], "\n")
			print("(3) Minimum number :", nums[0], "\n")
			print("※  Origin List :", origin_nums, "\n")
			print("※  Sorted List :", nums)
			print("---------------------------------------\n")

		elif (user == 2):
			print("\nSelect one of the following file.")
			print("(1) test1.txt")
			print("(2) test1_200.txt")
			print("(3) test1_500.txt")
			file = input("Please enter a integer between 1 to 3 : ")

			if file == "1":
				f = open("test1.txt")
			elif file == "2":
				f = open("test1_200.txt")
			elif file == "3":
				f = open("test1_500.txt")
			else:
				print("\nInput Error!")
				print("---------------------------------------\n")
				continue

			size = int(f.readline().replace("\n", ""))
			nums = f.readline().replace("\n", "").split()
			nums = [float(i) for i in nums]
			origin_nums = nums.copy()
			f.close()

			insert_sort(nums)

			print("\n----Quick Sort-------------------------")
			print("(1) The number of all numbers :", len(nums), "\n")
			print("(2) Maximum number :", nums[-1], "\n")
			print("(3) Minimum number :", nums[0], "\n")
			print("※  Origin List :", origin_nums, "\n")
			print("※  Sorted List :", nums)
			print("---------------------------------------\n")
		elif (user == 3):
			print("\nGoodbye!\n")
			break
		
		else:
			print("\nInput Error!")
			print("---------------------------------------\n")
			continue

	except:
		print("\nInput Error!")
		print("---------------------------------------\n")
		continue