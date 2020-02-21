list_with_1=[]
number=int(input())
binary_number=bin(number)
list=list(binary_number)
for i in list:
    if i=="1":
        list_with_1.append(i)
print(len(list_with_1))

