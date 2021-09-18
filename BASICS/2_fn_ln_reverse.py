#Prompt user for first, last names and print them in reverse order.

##########################1st way
#By considering the first and last names have to print as lastname follwed by its first name
print("\n***** 1st way *****")
x = input("enter your first name:\n")
y = input("enter your last name:\n")
print("your name is:\n" + x+y)
print("your name in reverse order is:\n" + y+x)


# ###########################2nd way
# #By considering all the letters involved in the given names has to be printed in reverse order
print("\n***** 2nd way *****")
a,b,c,d = "kaki"
print("your first name in reverse order is \n"+d+c+b+a)
e,f,g,h = "gaya"
print("your last name in reverse order is:\n"+ h+g+f+e)


###########################3rd way
#By using functions
print("\n***** 3rd way *****")
def name(m,n):
    print("your name in reverse oder is:\n" + n+m)
m,n = input().split(",")
name(m,n)