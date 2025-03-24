import random
lst = [random.randint(1,31) for i in range(50)]
print(lst)
unique_lst = []
for i in lst:
    if i in unique_lst:
        pass
    else:
        unique_lst.append(i)

print("List of unique numbers is :")
print(unique_lst)        
