first=8
second=2
third=3
if first==second==third:
    print(first,second,third)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)