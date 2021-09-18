######################## 1st way 
print("\n***** 1st way *****\n")
num = int(input("enter a number:\n"))
str = input("enter a string:\n")
print(num*str)

######################## 2nd way 
print("\n***** 2nd way *****\n")
a= int(input("enter a number:\n"))
b = input("enter a string:\n")
x = ""
for i in range(a):
   x += b
print(x)


######################## 3rd way 
def func(st, z):
   result = ""
   for i in range(z):
      result = result + st
   return result

print("\n by already taken inputs:\n")
print(func('gaya ', 3))
print(func('-kaki-', 5))
print(func('@Applines@ ', 2))
