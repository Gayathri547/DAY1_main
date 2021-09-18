############ 1st way without using functions
print("***** 1st way *****")
x = input("enter the digit you want to copy:\n")
y = int(input("enter your number:\n"))
l = list(x*y)
print(l)
sum = 0
for i in l:
    sum += int(i)
print(sum)

############ 2nd way by using functions
print("***** 2nd way *****")
def fun1(a1,a2):
    l2 = list(d*n)
    print(l2)
    sum2 = 0
    for j in l2:
        sum2 += int(j)
    print(sum2)
d = input("enter the digit you want to copy:\n")
n = int(input("enter your number:\n"))
fun1(d,n)

