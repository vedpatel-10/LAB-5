import random
random_numbers = [random.randint(1,100) for i in range(20)]
print(random_numbers)

number = int(input("Enter a number: "))
print("total count :"+ str(random_numbers.count(number)))
for i,ele in enumerate(random_numbers):
    if ele == number:
      print(i,ele)
