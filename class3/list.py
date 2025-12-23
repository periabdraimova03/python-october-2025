# Using the while loop keep asking the user to input an integer value 
# till the sum of those values reaches 100 or above. 
# Don’t forget to store all those values and print the condition was met. 
# (Hint: Use a list to store all the values)

sum = 0
list1 = []

while sum < 100:
    num = int(input("Enter the number: "))
    sum += num
    list1.append(num)
print(list1)     