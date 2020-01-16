

# Function to do insertion sort 
def insertion_sort(arr:list  = [4,8,3,6,23,90,2] ): 

    if len(arr) < 0 : raise ValueError("Array too small")
    if len(arr) <= 1 : return arr
    
    ret_arr = list(arr)

    # Traverse through 1 to len(arr) 
    for i in range(1, len(ret_arr)): 
  
        key = ret_arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < ret_arr[j] : 
                ret_arr[j + 1] = ret_arr[j] 
                j -= 1
        ret_arr[j + 1] = key

    return ret_arr 

def bucket_sort( arr:list  = [4,8,3,6,23,90,2] ):
    
    n = len(arr)

    if n < 0 : raise ValueError("Array too small")
    if n <= 1 : return arr
    
    #create a list of lists:
    ret_arr = []
    bucket = [[]] * n
    maxVal = max(arr)

    # fill the buckets
    for i, item in enumerate(arr):
        index = round((n - 1) * item / maxVal)
        print("the index "+str(i)+" is: "+str(index)+" and the val is: "+str(item))
        bucket[index] = bucket[index] + [item]
    print('the bucket is {}'.format(bucket))

    #check if they are all clustered in one bucket

    # order each individual bucket and concatenate to the result:
    for index, element in enumerate(bucket):
        #ret_arr += bucket_sort(element) # this only works if there is no repeated values
        ret_arr += insertion_sort(element) 
        
    return ret_arr


if __name__ == '__main__': 
    a = [1,3,7,5,2,8,0,4,3,78,3]
    
    sorted = insertion_sort(a)
    print("insertion sort test: ")
    print(a)
    print(sorted)

    sorted = bucket_sort(a)
    print("bucket sort test: ")
    print(a)
    print(sorted)

