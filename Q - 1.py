odd_num = [3,71,25,35,7]
even_num = [4,84,64,46]
odd_num.pop(2)                    # removing element at 2nd index
odd_num = [3,71,*even_num,35,7]   # inserting even no. list at 2nd index and unwraping it 
print(odd_num)
odd_num.sort()                    # sorting the list 
print("sorted list :")
print(odd_num)