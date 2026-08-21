B MURALI PRASAD
KUB25EEE610 
21\08\2026



'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 7, 89]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)'''

'''text = "university"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)'''

'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)'''

'''numbers = [-1, 3, 34, -8, -9, 1]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)'''

'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num in list3:
        common.append(num)

print("Common elements:", common)'''

'''numbers = [3, 10, 12, 54, 75, 89, 25, 23]

for num in numbers:
    if num % 3 != 0:
        print(num)'''
        
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

numbers.sort()

print("Second smallest:", numbers[1])'''

'''text = "university"

count = 0

for char in text:
    count += 1

print("Number of characters:", count)'''

'''numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)'''

'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

repeating = []

for num in list1:
    if num in list2:
        repeating.append(num)

print("Repeating values:", repeating)'''

'''arr = [10, 3, 5, 6, 7, 8, 9, 24, 3, 6, 7, 89]

smallest = min(arr)
largest = max(arr)

print("Smallest element:", smallest)
print("Largest element:", largest)'''

'''arr = [3, 10, 15, 54, 75, 89, 25, 23]

for num in arr:
    if num % 3 == 0 and num % 5 == 0:
        print(num)'''

'''arr = [-1, 3, 34, -8, -9, 1]

arr[0], arr[2] = arr[2], arr[0]

print(arr)'''

'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = list(set(list1) ^ set(list2))

print(result)'''

'''num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Square:", num ** 2)
else:
    print("Number is not divisible by 3")'''
    
    