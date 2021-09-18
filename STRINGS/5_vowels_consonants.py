########## 1st way for a sentence
print("***** 1st way *****")
print("\n")
vcount = 0
ccount = 0
sp = 0
str = input("enter your sentence:\n")
str = str.lower()
for i in range(len(str)):   
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1
    else:
        sp = sp+1
# print("Total number of vowel and consonant are" )
print("vowel count is:\n", vcount)
print("consonant count is:\n", ccount)
print("special characters count is:\n", sp)



########## 2nd way for a string
print("***** 2nd way *****")
print("\n")
v=0
c=0
s=0
st = input("enter your string:\n")
st = st.lower()
for i in range(len(st)):
    if st[i] == 'a' and 'e' and 'i' and 'o' and 'u':
        v = v+1
    else:
        c = c+1
print(v)
print(c)