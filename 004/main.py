# def hello_world():
    # print('Hello world!')
    # return "Hello world!"

# hello_world()
# print(hello_world())
# msg = hello_world()
# print(msg)

# def say_hello(name):
#     return f'Hello {name}!'

# print(say_hello("Amin"))


# def say_hello(name='Dear user'):
#     return f'Hello {name}!'

# print(say_hello(name='Amin'))

# def say_hello(fname, lname):
#     return f'Hello {fname} {lname}!'

# print(say_hello("Amin", 'Pourzare'))

# def say_hello(fname, lname, age=None):
#     if not age is None:
#         return f'Hello, {fname} {lname}. You are {age}'
#     else:
#         return f'Hello, {fname} {lname}.'

# print(say_hello("Amin", 'Pourzare', 31))


# def say_hello(fname, lname, height, age=None):
#     if not age is None and height > 170 :
#         return f'Hello, {fname} {lname}. You are {age}. Your height is {height}, You are tall.'
#     elif not age is None and height < 170 :
#         return f'Hello, {fname} {lname}. Your height is {height},'
#     else:
#         return f'You are secure person'

# print(say_hello(fname="Amin", lname='Pourzare', height=168, age=31))



# def say_hello(fname, lname, height, age=None):
#     if not age is None:
#         if height > 170 :
#             return f'Hello, {fname} {lname}. You are {age}. Your height is {height}, You are tall.'
#         else:
#             return f'Hello, {fname} {lname}. Your height is {height},'
#     else:
#         return f'You are secure person'

# print(say_hello(fname="Amin", lname='Pourzare', height=168, age=31))




# def get_len(data):
#     count = 0
#     for x in data:
#         count = count + 1
#     return count

# list_a = ['Amin', 'Ali', 'Jafar', 35]
# dict_a = {'first': 12, 'last': 96}
# print(get_len(dict_a))
# print(len(dict_a))


# def my_function(first, last, limit):
#     list_a = []
#     for x in range(first,last):
#         if x%limit == 0:
#             list_a.append(x)
    
#     return list_a
# result = my_function(1,10000,213)
# print(len(result))

def sum_number(number):
    x = 0
    y = number
    limit = str(number)
    for i in len(limit):
        if y < 10:
            x += y
            break
        x += y%10
        y =  y%10
    return x

print(sum_number(213))

