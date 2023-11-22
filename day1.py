print('.................remove dulicate......................')
# lst = [1,2,6,4,8,9,3,57,4,2,22,57]
# set_a = set(lst)
# print(lst)
# print(sorted((set_a)))
print('................. remove duplicates......................')
# # another aproach
# lst = [1,2,6,4,8,9,3,57,4,2,22,57]
# rmv_dpl = []
# for i in lst:
#     if i not in rmv_dpl:
#         rmv_dpl.append(i)
# print(rmv_dpl)
print('.................chnage first vowel word in string......................')
# str = 'sivarama'
# vowels = 'aeiou'
# change = 'h'
# prt = 0
# change_w = ''
# for i in str:
#     if i.lower() in vowels:
#         prt+=1
#         if prt == 1:
#             change_w+=change
#         else:
#             change_w+=i
#     else:
#         change_w+=i
# print(change_w)
print('..................polindrome.....................')
# polndrome = 'smoms'
# n = polndrome[::-1]
# if polndrome == n:
#     print('polindrome')
# else:
#     print('not polindrome')
print('.................delete key in dictionary......................')
# dict_a = {'a':'1','b':'2','c':'3'}
# del dict_a['a']
# print(dict_a)
print('..................print even and odd numbers.....................')
# numbers = [1,2,3,4,5,6,8,10,33,67,23,34,79,72]
# even_n = []
# odd_n = []
# for i in numbers:
#     if i%2==0:
#         even_n.append(i)
#     else:
#         odd_n.append(i)
# print(even_n)
# print(odd_n)
print('..................print prime numbers.....................')
# using for loop print prime numbers
# n = 20
# prime_num = []
# for i in range(2,n+1):
#     count = 0
#     for j in range(2,i+1):
#         if i%j==0:
#             count+=1
#     if count==1:
#         prime_num.append(i)
# print('Prime numbers: ',prime_num)
print('..................print prime numbers.....................')
# using while loop print prime numbers
# n1 = 20
# prime_num1 = []
# m = 2
# while m < n1+1:
#     count1 = 0
#     for k in range(2,m+1):
#         if m%k==0:
#             count1+=1
#     if count1==1:
#         prime_num1.append(m)
#     m+=1
# print(prime_num1)
print('...................print upper,lower,numbers,symbols separatley....................')
# n = 'sivaRAMA1234?><'
# upper_ltr = ''
# lower_ltr = ''
# numbers = ''
# symbols = ''
# for i in n:
#     if i.islower():
#         lower_ltr+=i
#     elif i.isupper():
#         upper_ltr+=i
#     elif i.isdigit():
#         numbers+=i
#     else:
#         symbols+=i
# print('lower ',lower_ltr)
# print('upper: ',upper_ltr)
# print('numbers: ',numbers)
# print('symbols: ',symbols)
print('..................change first and last letters in string.....................')
# word = 'sivarama'
# l = len(word)
# first_word = 'Sh'
# last_word = 'A..'
# new_wrd = ''
# for i in range(l):
#     if 0 == i:
#         new_wrd+=first_word
#     elif l-1 == i:
#         new_wrd+=last_word
#     else:
#         new_wrd+=word[i]
# print(new_wrd)
# print(word)
print('..................fibonacci.....................')
# def fibnoci(n):
#     if n==1:
#         return 1
#     else:
#         return n * fibnoci(n-1)
# n = 5
# result = fibnoci(n)
# print(result)
# .............fibonacci series...................
# n = 10
# first = 0
# second = 1
# for i in range(n):
#     if i <= 1:
#         result  = i
#     else:
#         result = first + second
#         first = second
#         second = result
#     print(result)
print('..................Write a program to reverse an integer in Python.....................')
# n = 123456789
# n_str = str(n)
# reverse_n = n_str[::-1]
# print(reverse_n)
# print(n)
print('.................check armstrong number......................')
# n = 500
# for i in range(1,n+1):
#     arm_add=0
#     for j in str(i):
#         arm_add+= int(j)**3
#     if arm_add == i:
#         print(f'Armstrong number{i}')
#     else:
#         print(f'Not armstrong number{i}')
print('...................polindrome by unsing recussive fun....................')
# def polindrome_num(n):
#     num = n[::-1]
#     return num
# number = '331133'
# result = polindrome_num(number) 
# if result == number:
#     print('polindrome')
# else:
#     print('not a polindrome')
print('.................print binary number......................')
# number = 50
# while number>0:
#     num = number%10
#     if num!=0 or num!=1:
#         print('not a binary number')
#         break
#     number = number//10
#     if num==0:
#         print('number is binary')
print('..................find highest integer....................')
# a = 27
# b = 65
# c = 37
# highest_val = 0
# if a > b and a > c:
#     highest_val = a
# elif b > a and b > a:
#     highest_val = b
# else:
#     highest_val = c
# print(highest_val)
print('.................swapcase without using third value......................')
# a = 3
# b = 5
# a = a - b
# b = b + a
# a = b - a
# print(a)
# print(b)
print('..................swapcase with using third value........................')
# a = 10
# b = 20
# third_val = a
# a = b
# b = third_val
# print(a)
# print(b)
print('.................factorial of n.................')
# n = 10
# fact_n = 1
# for i in range(1,n+1):
#     fact_n*= i
# print(fact_n)
print('.............................................')

