print ("BINARY SEARCH METHOD\n")
def bsm(arr,start,end,num):
    if end>=start:
        mid=start+(end-start)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bsm(arr,start,mid-1,x)
class Array:

    def __init__(self,array,number):
        self.lst = sorted(array)
        self.number = number
    def binary_search(self,lst,n,start,end):

        if start <= end:
            mid = (end + start) // 2
            if lst[mid] == n:

                return f'position: {mid}'
            elif lst[mid] > n:
                return binary_search(lst,n,start,mid-1)
            else:
                return binary_search(lst,n,mid + 1,end)
        else:
            return bsm(arr,mid+1,end,x)
    else:
            return -1


    def linear_search(self,lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return f'Position :{i}'
        return -1
arr=[10,27,36,49,58,69,70]
x=int(input("Enter the number to be searched : "))
result=bsm(arr,0,len(arr)-1,x)
if result != -1:
    print ("Number is found at ",result)
else:
    print ("Number is not present\n")

print ("Linear Search\n")
def linearsearch(arr, x):   
   for i in range(len(arr)):       
      if arr[i] == x:          
        return i    
   return -1 
arr = ['t','u','t','o','r','i','a','l'] 
x = input("enter character you want to search: ") 
print("element found at index "+str(linearsearch(arr,x)))

    def run_search(self):
        while True:
            print('Select the searching algorithm:')
            print('1. Linear Search.')
            print('2. Binary Search.')
            print('3. quit.')
            opt = int(input('Option: '))
            if opt == 2:
                print(search.binary_search(self.lst,self.number,0,len(lst)-1))
            elif opt == 1:
                print(search.linear_search(self.lst,self.number))
            else:
                break


lst = [1,2,3,4,5,6,7,8]
number = 4
search = Array(lst,number)
search.run_search()    
