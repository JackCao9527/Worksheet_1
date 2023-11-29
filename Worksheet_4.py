def is_year(year):
  if year % 4 == 0:
    return True
  else:
    return False
x = int(input("please enter a year: "))
print(is_year(x))

def is_even():
  num = int(input("Enter an number: "))
  if num % 2 == 0:
    return(num, "is an even number")
  else:
    return(num, "is not an even number")

print(is_even())

number = 0
for i in range (1, 10 + 1):
    number += i ** 2
print (number)

def fractions():
  total = 0
  for i in range (1, 10 + 1):
    numerator = i
    denominator = i + 1
    total += numerator / denominator
  return total
print (fractions())

def odd_fractions():
  total = 0
  for i in range (1, 97 + 1, 2):
    numerator = i
    denominator = i + 2
    total += numerator / denominator
  return total
print(odd_fractions())

def functions():
  m = int(input("please enter the value of m: "))
  n = 0
  while n ** 2 <= m:
    n += 1
  print ("the value of n is:  n^2 > m is:", n)
functions()

def count_digits(number):
  count = 0
  while number != 0:
    count += 1
    number //= 10
  return count
number = int(input("enter a number: "))
digit_count = count_digits(number)
print (digit_count)
#
def is_the_number_exact_same(list1, list2):
    if sorted(list1) == sorted(list2):
        return ("The two lists have the same value")
    else:
        return ("The two lists do not have the same value")

user_input1 = input("Enter the value of User_input1: ")
list1 = [int(x) for x in user_input1.split(" ")]
user_input2 = input("Enter the value of User_input2: ")
list2 = [int(x) for x in user_input2.split(" ")]
print(is_the_number_exact_same(list1, list2))

def index_of_min(lst):
    if not lst:
        breakpoint()
    min_value = lst[0]
    min_index = 0

    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i
    return min_index

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
result = index_of_min(numbers)
if result is not None:
    print(f"The index of the smallest number is {result}")
else:
    print("The list is empty.")

def main():
    user_input = input("Enter a list of real numbers separated by spaces: ")
    numbers = [float(x) for x in user_input.split()]
    summation = 0
    for number in numbers:
        summation += number
    print(f"The summation of the numbers is: {summation}")
main()

