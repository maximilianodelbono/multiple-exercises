a="Hi, this is Maxi"

def reverseit(sg):
    return(a[::-1])

print(reverseit(a))


def reverseit_hard(sg):
    dictionary_vals = {}
    sizeSG = len(sg)
    #result=''
    for i in range(0,sizeSG):
        dictionary_vals[i]=sg[sizeSG-1]
        sizeSG-=1

    return(''.join(dictionary_vals.values()))
    #return ''.join(map(str,dictionary_vals.values()))
    #return(result.join(dictionary_vals.values()))
print(reverseit_hard(a))

def reverse(sg):
  mylist=[]
  for i in range(len(sg)-1,-1,-1):
    mylist.append(sg[i])
  return ''.join(mylist)

x=reverse(a)
print(x)
