#1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function
def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("Eric")

#2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    for num in range(1,101):
        if num%2 != 0:
            print(num)
first_odds()


#3 Please write a Python function, max_num_in_list to return the max number of a given list
def max_num_in_list(a_list):
    return max(a_list)  
print(max_num_in_list([10, 23, 56, 67, 99]))

# #4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if (a_year % 4 == 0)  and (a_year % 100 != 0) or (a_year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap        
print(is_leap_year(2000))
print(is_leap_year(1800))

# #5 Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        x = a_list[i]
        y = a_list[i+1]
        if x +1 != y:
            return False
    return True

print(is_consecutive([2,3,4,5,6,7]))
print(is_consecutive([1,2,4,5]))


    