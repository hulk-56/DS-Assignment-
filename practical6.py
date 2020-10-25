#selection sort
def selection_sort(num):
        for i in range(len(num)):
            lowest_value_index=i
            for j in range(i+1,len(num)):
              if num[j]<num[lowest_value_index]:
                         lowest_value_index=j  
                         num[i],num[lowest_value_index]=num[lowest_value_index],num[i]



class Sorting:

    def __init__(self,lst):
        self.lst = lst

    def bubble_sort(self,lst):
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i] < lst[j]:
                    lst[i],lst[j] = lst[j],lst[i]
                else:
                    pass
        return lst

list=[1,2,3,4]
selection_sort(list)
print(list)
    def selection_sort(self,lst):
        for i in range(len(lst)):
            smallest_element = i
            for j in range(i+1,len(lst)):
                if lst[smallest_element] > lst[j]:
                    smallest_element = j
            lst[i],lst[smallest_element] = lst[smallest_element],lst[i]
        return lst

#insertion sort
def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key
# main
arr = ['t','u','t','o','r','i','a','l']
insertionSort(arr)
print ("The sorted array is:")
for i in range(len(arr)):
   print (arr[i])

#bubble sort
def bubble_sort(num):
     swap=True
     while swap:
            swap=False
            for i in range(len(num)-1):
                 if num[i]>num[i+1]:
                       num[i],num[i+1]=num[i+1],num[i]
                       swap=True


 list=[23,14,66,8,2]
bubble_sort(list)
print(list)
    def insertion_sort(self,lst): 
        for i in range(1, len(lst)): 
            index = lst[i] 
            j = i-1
            while j >= 0 and index < lst[j] : 
                    lst[j + 1] = lst[j] 
                    j -= 1
            lst[j + 1] = index 
        return lst

    def run_sort(self):
        while True:
            print('Select the sorting algorithm:')
            print('1. Bubble Sort.')
            print('2. Selection Sort.')
            print('3. Insertion Sort.')
            print('4. Quit')
            opt = int(input('Option: '))
            if opt == 1:
                print(sort.bubble_sort(self.lst))
            elif opt == 2:
                print(sort.selection_sort(self.lst))
            elif opt == 3:
                print(sort.insertion_sort(self.lst))
            else:
                break
lst = [12,43,53,2,5,98,57,87,12] 
sort = Sorting(lst)
sort.run_sort()
