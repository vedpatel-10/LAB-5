import random
lst = [random.randint(-50,50) for i in range(30)]
print(lst)
pos_list = []
neg_list = []

for i in lst:
    if i >0:
        pos_list.append(i)
    elif i<0:
        neg_list.append(i)
    
print("List with positive numbers: ")
print(pos_list)

print("List with negative numbers: ")
print(neg_list)

#OUTPUT:
# [-26, 47, 9, 14, 39, 43, -15, 17, 7, 29, -8, -47, -36, 10, -16, -43, -39, 11, -34, 24, 22, -32, 19, 13, -42, 12, -22, 34, 44, -44]
# List with positive numbers:
# [47, 9, 14, 39, 43, 17, 7, 29, 10, 11, 24, 22, 19, 13, 12, 34, 44]
# List with negative numbers:
# [-26, -15, -8, -47, -36, -16, -43, -39, -34, -32, -42, -22, -44]
