a = input("enter your string:\n")
for i in a:
    if(a[:2] == "is"):
        print("no need to change")
        break
    else:
        print("is"+a)
        break

