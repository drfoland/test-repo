### This is my own insertionSort code completed as an eLearning exercise.


"""
main() function is used to demonstrate the sort() function
using a randomly generated list.
""" 
def main():
	### List Initialization
	from numpy import random

	LENGTH = 6

	list = []

	for num in range(LENGTH):
		list.append(random.randint(100))

	print("Unsorted List:")
	print(list)
	print()
	
	list = sort(list)
	
	print("Sorted List:")
	print(list)
	
"""
sort() is the implementation of a basic insertion sort
algorithm.
"""
def sort(list):
	### Beginning of Selection Sort Algorithm
	
	"""
	NEEDS TO BE UPDATED
	"""
	
	
	return list	
	
	
if __name__ == "__main__":
	main()

	