################## 1st way
print("***** 1st way *****")
a=input("enter a string\n")
b=input("enter the character that you want to search")
print(a.count(b))

################## 2nd way
print("***** 2nd way *****")
c = 0
x= input("enter a string:\n")
y = input("enter the character you want to search:\n")
for i in x:
    if i == y:
        c += 1
print(c)

