def bubbleSort(array):
    print("this is the function")
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selectioSort(array):
      n = len(array)
      for i in range(n):
        min = i
        for j in range(i+1,n):
              if array[j]<array[min]:
                min = j
              array[i],array[min]=array[min],array[i]
      return array


def insertionSort(array):
     n = len(array)

     for i in range(1,n):
          key = array[i]
          j = i-1
            # now the from 0 to j-1 the array is sorted now we just want to put the key at the right place

          while j >=0 and array[j] > key :
               array[j+1] = array[j]
               j = j-1
          
          array[j+1] = key
     return array

               
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_Sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_Sort(arr, left, mid)
        merge_Sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        return arr
def mergeSort(array):
    return merge_Sort(array, 0, len(array)-1)
    


def printarray(array):
      for i in array:
            print(i)

# if __name__ == "__main__":
#     bubbleSort()