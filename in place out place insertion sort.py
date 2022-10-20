"""
Ans 1.
An "In-Place" sorting algorithm is algorithm whose space complexity
lies between O(1) and O(logn) both included.
We can say an in-place algorithm is an algorithm that does need a
small extra space and produces an output in the same memory that
contains the data by transforming the input ‘in-place’.Where as an 
"Out-Place" sorting algorithm is algorithm whose space complexity is 
greater than O(logn).
"""
def insertion_sort_IP(arr,n):
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key


def insertion_sort_OP(arr,si,ei):
    if si == ei:
        return
    j = si+1
    temp = arr[j]
    while si>=0:
        if arr[si]>temp:
            arr[si+1] = arr[si]
            si-=1

        if si == -1:
            arr[0]=temp
            break
        if arr[si]<=temp:
            arr[si+1]=temp
            break

def pfun(arr,n):
    for k in range(n):
        print(arr[k],end=' ')

arr = []
arr2 = []

n = int(input("Enter number of elements in array: "))
#a = print("Enter elements of array one by one:")
for i in range(n):
    a = int(input("Enter elements of array one by one:"))
    arr.append(a)

arr2 = arr[:]

print("Array before sorting: ")
pfun(arr,n)

insertion_sort_IP(arr,n)
print("\nArray after sorting using in-place algorithm:")
pfun(arr,n)

insertion_sort_OP(arr2,0,n-1)
print("\nArray after sorting using out_place algorithm:")
pfun(arr,n)

"""
Ans 3.

In-place techniques have lesser space complexity but are difficult to 
apply in algorithm whereas out-place techniques are easy to aplly but 
increases the space complexity of algorithm.
For exapmle if we want to reverse an array then its in-place algorithm
will be swaping the first and last element of array until we reach the 
middle of array,If we want to solve the same problem using out-place 
algorithm we have to create one extra array of same size and copy 
elements of original array from back to the front of new array,this 
algorith increases the space complexity to O(n) as we have creaed an 
extra array.
IN-PLACE algorithm are used in Bubble sort, Selection Sort, Insertion Sort, Heapsort.
NOT IN-PLACE algorithm is used in Merge Sort.
Because merge sort requires O(n) extra space.
"""







