print('...............count given word in string................')
# string = input('enter the value:')
# character = input('enter the character:')
# count_character = string.count(character)
# print(count_character)
print('..............square and cube the given numbers...............')
# n = [1 , 2, 3, 5, 8, 6, 7, 16]
# sqr_even = []
# cube_odd = []
# for num in n:
#     if num%2==0:
#         sqr_even.append(num**2)
#     else:
#         cube_odd.append(num**3)
# print(f'square even num: {sqr_even}')
# print(f'cube obb numbers: {cube_odd}')
print('................LCM of two numbers.................')
# n = 4
# m = 10
# if n > m:
#     greater_num = n
# else:
#     greater_num = m
# while True:
#     if greater_num%n==0 and greater_num%m==0:
#         lcm = greater_num
#         break
#     greater_num+=1
# print(lcm)
print('...............square root.............')
# n = [26,81,25,64,98,27,48]
# sqr_root = []
# for i in n:
#     num = round(i**0.5,2)
#     sqr_root.append(num)
# print(f'square root: {sqr_root}')
print('................convert decimal num to binary....................')
# n = 29
# binary = ''
# while n > 0:
#     reminder = n%2
#     binary = str(reminder) + binary
#     n = n//2
# print(binary)
print('...............octal no for given number....................')
# def octal_number(dec):
#     if dec==0:
#         return ""
#     quotient = dec//8
#     reminder = dec%8
#     return octal_number(quotient) + str(reminder)
# decimal = 157
# ocatal = octal_number(decimal)
# print(f'octal no: {ocatal},for given {decimal}')
print('...................find leap year.....................')
# n = [2000,2004,2007,2022,2018,2019]
# for year in n:
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 print(year,'Leap year')
#             else:
#                 print(year,'non leap year')
#         else:
#             print(year,'leap year')
#     else:
#         print(year,'non leap year')
print('..............swap positons.............')
# n = [29,18,30,86]
# index1 = 1
# index2 = 3
# n[index1],n[index2] = n[index2],n[index1]
# print(n) 
print('...............fahrenheit and celsius convertion.................')
# CELSIUS TO FAHRENHEIT: ~~~[(C * 1.8) + 32]~~~~
# FAHRENHEIT TO CELSIUS: ~~~[((F - 32) * 5)/9]~~~~

# n = ['97F','65C','30C','85C','100F','50F']
# for deg in n:
#     if deg[-1]=='C':
#         cel_to_fah = str(round(int(deg[:-1])*1.8+32,2))
#         print(f'{deg} to convert {cel_to_fah}F')
#     else:
#         fah_to_cel = str(round((int(deg[:-1])-32)*5/9,2))
#         print(f'{deg} to convert {fah_to_cel}C')
print('...............remove given character in string.................')
# n = 'shivaram'
# rmv = 'h'
# new = ''
# for i in n:
#     if rmv == i:
#         continue
#     else:
#         new+=i
# print(new)
print('...............delete vowels in string...............')
# n = 'bhichAgadumovIe'
# rmv_vowel = ''
# for i in n:
#     if i.lower() in ('a','e','i','o','u'):
#         continue
#     else:
#         rmv_vowel+=i
# print(rmv_vowel)
print('...............highest frequency character...................')
# n = 'sivaramakrishna'
# new = ''
# frequency = ''
# count_n = []
# for i in n:
#     if i not in new:
#         new+=i
# for j in new:
#     count_n.append(n.count(j))
# for k in new:
#     count = n.count(k)
#     if count == max(count_n):
#         frequency+=k+" "
# print(count_n)
# print(frequency)
print('..............find vowel in insert "_"............')
# n = 'sivarama'
# m = ''
# for i in n:
#     if i in ('a','e','i','o','u'):
#         m+="_"
#     else:
#         m+=i
# print(m)
print('............use join() to join two strings...............')
# a = 'sivarama'
# b = 'krishna'
# result = ' '.join([a,b])
# print(result)
print('..............repeated character in string...............')
# n = 'repeated character'
# non_rep = ''
# for i in n:
#     rep = n.count(i)
#     if rep == 1:
#         non_rep += i
# print(non_rep)
print('...........ascending and descending.............')
# n = [1,8,9,2,19,38,7,4,43,65]
# ascending = sorted(n)
# print(ascending)
# descending = sorted(n,reverse=True)
# print(descending)
print('.................repeated numbers in list..................')
# list_a = [1,3,2,4,6,7,3,5,6,8,4,9,3]
# max_l = []
# for i in list_a:
#      l = list_a.count(i)
#      if l > 1:
#          if i not in max_l:
#             max_l.append(i)
# print(max_l)
print('..............................')
