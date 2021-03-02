a = [1, 2, 3, 4]
# print(a[1:].__len__())
# print(len(a[1:]))
a.append(5)
# print(a)
a.insert(1, 6)
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# a.pop(1)
# print(a)

# a.clear()
# print(a)

# b = a
b = a.copy()
# b = a != b = a.copy()
print("b is", b)

a.append(3)
a.append(3)
print("a is", a)
# print(a.count(3))

# print(a.index(6))
# c = a.index(3, 4, -1)
# print(c)

# a.remove(3)
# print(a)

# print(b)
# a = a + b
# print(a)

d = a + b
#
# print(d)
e = []
e.append(a)
e.append(b)
# print(e)
# print(len(e))
# print(a)
# a.__add__([7])
# print(a)
# for x in a:
#     print(x)
# aa = len(a)
# print(aa)
for y in range(len(a)):
    print(a[y])
bb = []
for num in range(0, 100, 3):
    bb.append(num)
print(bb)
print(len(bb))
