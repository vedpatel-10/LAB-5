fah_temp = [70,100,67,102,89]
cel_temp = []

for i in fah_temp:
    x = (5/9) * (i -32)
    cel_temp.append(x)

print(cel_temp)    

#OUTPUT:
# [21.11111111111111, 37.77777777777778, 19.444444444444446, 38.88888888888889, 31.666666666666668]
