arr_1=[0,3,4,31]
arr_2=[4,6,30]
arr_res=[]

for i in arr_1:
    for j in arr_2:
        if(i<j):
            arr_res.append(i)
            break
        elif (i==j):
            arr_res.append(i)
            arr_res.append(j)
            break
        elif (i>j):
            arr_res.append(j)
            arr_res.append(i)
            break
print(arr_res)
