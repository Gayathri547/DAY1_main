############################## 1st way
#By considering the ::
print("\n***** 1st way *****")

names = input("enter your first and last names:\n").split(",")
print('Original List:', names)

reversed_list = names[::-1]
print('Updated List:', reversed_list)
print("\n")


############################## 2nd way
#By using append()
print("\n***** 2nd way *****")
fn=input("enter your first name\n")
cfn=list(fn)
print(cfn)
ln=input("enter your last name\n")
cln=list(ln)
print(cln)
for i in cfn:
    cln.append(i)

print("your name in reverse order is ",cln)

############################## 3rd way
#By using reverse()
print("\n***** 3rd way *****")
a = input("enter your first and last names:\n").split(",")
a.reverse()
print(a)
