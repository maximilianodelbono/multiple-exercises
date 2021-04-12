class Array:
  def __init__(self):
    self.length=0
    self.data={}

  def __str__(self):
    return str(self.__dict__)

  def get(self,index):
    return self.data[index]

  def push(self,item):
    self.data[self.length]=item
    self.length+=1

  def pop(self):
    lastitem = self.data[self.length-1]
    del self.data[self.length-1]
    self.length-=1
    return lastitem

  def delete(self,index):
    deleteditem = self.data[index]
    print("you will delete ",deleteditem)
    #from the item i am gonna delete to the last item (it would not be correct to edit the index of the ones before the one i want to delete)
    for i in range(index,self.length-1): #build range from index to length
      print("grabing ",i," turning it into: ",i+1)
      self.data[i] = self.data[i+1] #change each element's index to the (idx+1)
      print(self.data)

    del self.data[self.length-1] #deletes the last one
    self.length-=1 #reduce the value in the __init__ by 1
    return deleteditem

arr=Array()
arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
print("will delete: ",arr.get(3))
arr.delete(3)
print(arr)
