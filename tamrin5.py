print("enter the seconds")
x=int(input())
h=int(x/3600)
m=int((x-(h*3600))/60)
s=(x-(h*3600+m*60))
print(h,":",m,":",s)
