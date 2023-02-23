num1 = 10
num2 = 20


#print(bin(num1)[2:])
#print(bin(num2)[2:])
#print(bin(num1 & num2)[2:])

num3 = num1 & num2 
    
print("EL resultado AND de %s")
print("es %s") 
      print(bin(num3)[2:])

num4 = num1 | num2

print("EL resultado OR de su numero 1 y 2 es %s ")
print(bin(num4)[2:])

num5 = num1 ^ num2

print("EL resultado XOR de su numero 1 y 2 es %s ")
print(bin(num5)[2:])