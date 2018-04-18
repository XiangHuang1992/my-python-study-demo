a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = filter(lambda x: x > 4, a)

#for num in b:
 #   print(num)

c = map(lambda x: x*x, [y for y in range(10)])

for n in c:
    print(n)

d = map(lambda x: x * 2, range(1, 5))
print(list(d))