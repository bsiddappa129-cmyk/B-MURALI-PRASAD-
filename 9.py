# # # # NAME : B MURALI PRASAD
# # # # USN : KUB25EEE610
# # # 
# # # DATE : 22/08/2026

# # # nums = [3, 10, None, 15, 54, 75, 25, 23]

# # # found = False

# # # for num in nums:
# # #     if num is not None and (num % 3 == 0 or num % 5 == 0 or num % 8 == 0):
# # #         print(num)
# # #         found = True

# # # if not found:
# # #     print("none")
    
# # # nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# # # smallest = min(nums)
# # # largest = max(nums)

# # # print("Smallest:", smallest)
# # # print("Largest:", largest)

# # # nums = [-1, 3, 34, -8, -9, 1]

# # # nums[0] = 100

# # # print(nums)

# # # list1 = [1, 2, 3, 4]
# # # list2 = [3, 4, 5, 6]

# # # avg = (sum(list1) + sum(list2)) / (len(list1) + len(list2))

# # # print("Average:", avg)

# # # num = int(input("Enter a number: "))

# # # if num % 3 == 0:
# # #     num = num + 5

# # # print(num)

# # # nums = [3, 10, 15, 54, 75, 25, 23]

# # # for num in nums:
# # #     if num % 3 == 0 and num % 5 != 0:
# # #         print(num)

# # # nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

#  for num in nums:
#     if num > 30:
#          print(num)


# nums = [-1, 3, 34, -8, -9, 1]

# 1. Add an element
# nums.append(10)
# print("After append:", nums)

# 2. Remove an element
# nums.remove(34)
# print("After remove:", nums)

# 3. Insert an element
# nums.insert(1, 20)
# print("After insert:", nums)

# 4. Find length
# print("Length:", len(nums))

# 5. Find maximum
# print("Maximum:", max(nums))

# 6. Find minimum
# print("Minimum:", min(nums))

#  7. Sort the list
#  nums.sort()
#  print("Sorted:", nums)

#  8. Reverse the list
#  nums.reverse()
# print("Reversed:", nums)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# avg = sum(nums) / len(nums)

# print("Average:", avg)

# num = 1578693
# divisors = []

# for i in range(1, 11):
#     if num % i == 0:
#         divisors.append(i)

# print("Divisors:", divisors)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 % 5 == 0:
#     num1 = num1 ** 2

# if num2 % 5 == 0:
#     num2 = num2 ** 2

# print("First number:", num1)
# print("Second number:", num2)

# nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# prime = []
# even = []
# odd = []

# for num in nums:
#     # Even and odd
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

#     # Prime
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             prime.append(num)

# print("Prime numbers:", prime)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# nums = [-1, 3, 34, -8, -9, 1]

# result = []

# for num in nums:
#     if num >= 0 and num % 3 != 0:
#         result.append(num)

# print(result)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# total = sum(nums)
# count = len(nums)
# avg = total / count

# print("Sum:", total)
# print("Count:", count)
# print("Average:", avg)

# num = 1578693

# for i in range(1, 11):
#     if num % i == 0:
#         num = num - 100
#         print(i, "is divisible, result:", num)
#     else:
#         print(i, "is not divisible")


# word = "university"

# count = 0

# for ch in word:
#     if ch in "aeiou":
#         count += 1

# print("Vowel count:", count)

# nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# # Print 89
# print(89)

# # Add 59 at 9th index
# nums.insert(9, 59)

# print(nums)

# nums = [-1, 3, 34, -8, -9, 1]

# for num in nums:
#     print(num ** 2)
    
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# result = num1 // num2

# print("Floor division:", result)

# nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89, 7, 8, 54, 621, 57, 24, 3, 5, 6, 4]

# unique = []

# for num in nums:
#     if num not in unique:
#         unique.append(num)

# print("Unique values:", unique)  