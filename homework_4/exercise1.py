kit = [int(x) for x in input().split()]
n = kit[0]
m = kit[1]
myset_1 = set()
myset_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    myset_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    myset_2.add(i)
lok = myset_1 & myset_2
list1 = list(lok)
list1.sort()
for i in list1:
    print(i, end=" ")
