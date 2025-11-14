
#strinf slicing
def main():
    array=[0,1,2,3,4,5,67] #initials of the fib
    #insert into the array 
    array.append(1) #insert at the last 
    array.insert(2,12) #insert at the second position starts from 1 not from 0
    array.extend([12,13])
    #print(array)

    #remove 
    ele = array.pop()  # remove the index o element 
    #print("poped eleement :" , ele)

    array.remove(12) # remove 12 directly from the array

    del array[1:3]  #delete the slice from the array 

   # print(array)



    #List  Comprehension

    num = [2,3,4,68,8]
    #nums2 = [x+2 for x in num if x == 4] #it will store only the afected one
    def is_even(x):
        return x % 2 == 0
    nums2 = list(filter(is_even,num))   #filter(function, iterable)
    nums3 =  list(filter(lambda x:x+2== 4,nums2))
    nums4 = list (map(lambda x:x*12,num))
    print(nums4)

if __name__ == "__main__":
    main()