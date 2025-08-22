a=["niki","suji","mari","gill"]
mark=[[35,78,9,85],[33,78,47,57],[49,58,29,50],[40,59,30,78]]
per=[]
for i in mark:
    d=sum(i)//4
    per.append(d)
for i in range(4):
    print("{}.{}:{}%".format(i+1,a[i],per[i]))