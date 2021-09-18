############# 1st way
print("***** 1st way *****")
a = int(input("enter a number:\n"))
if a % 2 ==0:
    print("even")
else:
    print("odd")

############# 2nd way
print("*****  2nd way *****")
def fun1(x):
    if x%2 ==0:
        print("even")
    else:
        print("odd")
print(fun1(int(input("enter a number:"))))