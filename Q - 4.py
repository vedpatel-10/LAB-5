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