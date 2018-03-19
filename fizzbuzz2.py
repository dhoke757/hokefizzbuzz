import sys
inp = input("Enter a number: ")
n = int(inp)
count = 1

while (count <= n):
	if (count % 3 == 0 and count % 5 == 0):
		print("Fizzbuzz")
	elif (count % 3 == 0):
		print("Fizz")
	elif (count % 5 == 0):
		print("Buzz")
	else:
		print(count)	
	count = count + 1		
		