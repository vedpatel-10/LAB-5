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

#OUTPUT:
# [26, 9, 30, 17, 18, 25, 18, 14, 18, 22, 1, 18, 9, 28, 23, 12, 11, 29, 12, 13, 8, 29, 22, 1, 5, 23, 18, 13, 27, 24, 5, 31, 5, 29, 7, 19, 14, 21, 4, 4, 11, 13, 5, 23, 24, 8, 19, 27, 4, 19]      
# List of unique numbers is :
# [26, 9, 30, 17, 18, 25, 14, 22, 1, 28, 23, 12, 11, 29, 13, 8, 5, 27, 24, 31, 7, 19, 21, 4]
