import random
random_numbers = [random.randint(1,100) for i in range(20)]
print(random_numbers)

number = int(input("Enter a number: "))
print("total count :"+ str(random_numbers.count(number)))
for i,ele in enumerate(random_numbers):
    if ele == number:
      print(i,ele)

#OUTPUT:
# [37, 46, 90, 57, 16, 27, 64, 40, 94, 47, 36, 79, 29, 87, 74, 99, 18, 36, 45, 99]
# Enter a number: 27
# total count :1
# INDEX IS 5, VALUE IS 27
