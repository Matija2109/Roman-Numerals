##########################################################################
# The Roman Empire Strikes Back
#
# You are given a function int_to_roman that gets an integer n and returns
# a string with the Roman representation of n. In this task we will analyse
# Roman numerals.
##########################################################################

def int_to_roman(n):
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    thousands = (n // 1000) % 10
    r_ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    r_tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    r_hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    r_thousands = ['', 'M', 'MM', 'MMM']
    return r_thousands[thousands] + r_hundreds[hundreds] + r_tens[tens] + r_ones[ones]

##########################################################################
# Write a function longest_roman(a, b) that returns the length of the
# longest Roman numeral among all numbers n, where a <= n <= b.
#
# Examples:
#
#     >>> longest_roman(7, 7)
#     3
#     >>> longest_roman(13, 27)
#     5
#     >>> longest_roman(1, 887)
#     11
##########################################################################

def longest_roman(a, b):
    if a==b:
        print(len(int_to_roman(a)))
    else:
        l=[]
        max_len=-1
        res=None
        for i in range(a, b):
            roman=int_to_roman(i)
            l.append(roman)
            if len(roman)>max_len:
                max_len=len(roman)
                res=max_len
        print

##########################################################################
# The emporer also wants to know which Roman numeral are the longest.
# Write a function get_longest_roman(a, b) that will return a list of strings;
# strings are Roman numerals between a and b (including a and b) of maximal
# length.
# 
# Examples:
# 
#     >>> get_longest_roman(7, 7)
#     ['VII']
#     >>> get_longest_roman(13, 27)
#     ['XVIII', 'XXIII', 'XXVII']
#     >>> get_longest_roman(1, 887)
#     ['CCCLXXXVIII', 'DCCLXXXVIII', 'DCCCXXXVIII', 'DCCCLXXVIII', 'DCCCLXXXIII', 'DCCCLXXXVII']
##########################################################################

def get_longest_roman(a, b):
    if a==b:
        l=[]
        roman=int_to_roman(a)
        l.append(roman)
        print(l)
    else:
        l2=[]
        l3=[]
        max_len=-1
        res=None
        for i in range(a, b+1):
            roman=int_to_roman(i)
            l2.append(i)
            if len(roman)>max_len:
                max_len=len(roman)
                res=max_len
        for j in l2:
            k=int_to_roman(j)
            if len(k)==res:
                l3.append(k)
        print(l3)

##########################################################################
# The emporer has another task for you. He also wants you to write a function
# numbers_of_length(l) that gets an integer l as an argument. The function
# should return the list of all integers between 1 and 3999 (inclusive) whose
# Roman numerals are of length exactly l.
# 
# Examples:
# 
#     >>> numbers_of_length(1)
#     [1, 5, 10, 50, 100, 500, 1000]
#     >>> numbers_of_length(2)
#     [2, 4, 6, 9, 11, 15, 20, 40, 51, 55, 60, 90, 101, 105, 110, 150, 200, 400, 
#      501, 505, 510, 550, 600, 900, 1001, 1005, 1010, 1050, 1100, 1500, 2000]
#     >>> numbers_of_length(14)
#     [2888, 3388, 3788, 3838, 3878, 3883, 3887]
##########################################################################

def numbers_of_length(l):
    l2=[]
    for i in range(1, 4000):
        roman=int_to_roman(i)
        if len(roman)==l:
            l2.append(i)
    print(l2)

##########################################################################
# The emporer thinks that the functions you have programmed are really
# interesting. Here is the final quest for you. Write a function sum_roman(a, b, l)
# that return the sum of all integers between a and b (inclusive) whose
# corresponding Roman numerals are of length precisely l.
#
# Examples:
#
#     >>> sum_roman(1, 715, 1)
#     666
#     >>> sum_roman(3000, 3800, 14)
#     7176
#     >>> sum_roman(1000, 3000, 9)
#     660156
##########################################################################

def sum_roman(a, b, l):
    l2=[]
    for i in range(a, b):
        roman=int_to_roman(i)
        if len(roman)==l:
            l2.append(i)
    res=sum(l2)
    print(res)

sum_roman(1000, 3000, 9)
