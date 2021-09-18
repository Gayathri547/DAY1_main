print("\n*** NOTE: type exit to come out of the loop ***\n")
while 1:
    x= input("enter anything:\n")
    if(x=="exit"):
        break
    elif x.isnumeric():
        print("Number")
    elif x.isalpha():
        print("Alphabates")
    elif x.isalnum():
        print("Alphanumeric")
    else:
        print("It belongs to other category")


