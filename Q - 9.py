lst1 = [23,45,66,78,68,67,45]
lst2 = [23,76,4,81]

lst3 = [ i for i in lst1 if not(i in lst2)]
print(lst3)

#OUTPUT:
#[45, 66, 78, 68, 67, 45]
