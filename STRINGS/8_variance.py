# variance formula is ((diff between given 2 values)/first number) *100
a = int(input("enter 1st number:\n"))
b = int(input("enter 2nd number:\n"))
diff = b - a
var = (diff/a)*100
variance = int(var)
print("The variance for the given numbers is:")
print(variance)


x = int(input("\n enter the number you want to check:\n"))
for i in range(variance):
    if i == x:
        print("your number is within the range")



        
    