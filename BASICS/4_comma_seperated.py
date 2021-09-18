#by using split, it will generate a list by default
a = input("Input some comma seprated numbers : ")
list = a.split(",")
tuple = tuple(list)
print('Given values in list:',list)
print('Given values in tuple: ',tuple)
