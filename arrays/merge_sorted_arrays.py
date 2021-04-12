arr_1=[0,3,4,31,32]
arr_2=[4,6,30,60]
arr_res=[]

def mergeSortedarr(a,b):
    '''Funciton to sort and merge'''
    if len(a)==0 or len(b)==0:
        #print("one of the arrays is empty")
        return a+b
    i=0
    j=0

    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            arr_res.append(a[i])
            i+=1
        elif a[i]>b[j]:
            arr_res.append(b[j])
            j+=1
    print("•i",i,a[i:])
    print(b[j:])
    return arr_res+a[i:]+b[j:]

print(mergeSortedarr(arr_1,arr_2))
