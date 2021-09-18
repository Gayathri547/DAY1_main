######################### 1st way
print("***** 1st way *****\n")
fn=input("enter your first name\n")
cfn=tuple(fn)
print(cfn)
ln=input("enter your last name\n")
cln=tuple(ln)
print(cln)
print("your name in reverse order is",cln+cfn)


######################### 2nd way
print("***** 2nd way *****\n")

print("reverse of first name is", tuple(fn[::-1]))
print("reverse of last name is", tuple(ln[::-1]))