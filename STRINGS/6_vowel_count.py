v = 0
st = input("enter your string:\n")
st1 = st.lower()
dic = {}
for i in st1:
    if i in ('a','e','i','o','u'):
        v = v+1
        dic[i] = v
        
print("number of vowels are:\n", v)
print("dictionary is:", dic)