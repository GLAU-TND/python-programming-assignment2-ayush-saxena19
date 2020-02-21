from functools import cmp_to_key
list=[]
elements=int(input())
for i in range(elements):
    elements=int(input("enter the elements"))
    list.append(elements)
print("The original list is : " + str(list))
res = sorted(list, key=cmp_to_key(lambda i, j: -1
if str(j) + str(i) < str(i) + str(j) else 1))
print("The largest possible number : " + ''.join(map(str, res)))