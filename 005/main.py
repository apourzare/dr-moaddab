# *args -> list or tuple optional as param

# def info(fname, lname, age, *args):
#     if args:
#         fav = ''
#         for i in args:
#             fav += ', '.join(i)
#         return f'{fname} {lname} is {age} he favorits are {fav}'
#     else:
#         return f'{fname} {lname} is {age}'

# print(info("Amin", "Pourzare", 31))
# print(info("Amin", "Pourzare", 31, ['programming', 'blue', 'football', 'move']))

# **kwargs -> dictionary optional as param
# def info2(fname, lname, age, **kwargs):
#     if kwargs:
#         return f'Your gender is {kwargs["gender"]}, You are from {kwargs["country"]}'
#     else:
#         return 'Welcome'

# print(info2("Amin", "Pourzare", 31))
# print(info2('ali', 'hassani', 22, gender='Male', country='Iran'))


# for i in range(7,100,8):
#     print(i)

# j = 7
# while j < 100:
#     print(j)
#     j += 8

# list_a = ['ali', 'hammid', 'zahra']

# for i in range(len(list_a)):
#     print(list_a[i])

# for i in list_a:
#     print(i)

# j = 0
# while j < len(list_a):
#     print(list_a[j])
#     j += 1

import numpy
import requests