


def counting_sort( arr:list  = [4,8,3,6,23,90,2,-34], a:float = -100, b:float = 100):
    """
    this type of sort requires a fixed data limit [a, b]

    """
    if len(arr)<=0 : raise ValueError("Array too small")

    dic_arr = list(range(a, b + 1)) # value array of each posible value
    count_arr = [0] * len(dic_arr) # ceros array to store the count
    ret_arr = list(arr) # the return array ordered

    #print("dicctionary array: "+str(dic_arr))
    # count the number of times each value is repeated
    for value in arr:
        dic_index = dic_arr.index(value)
        count_arr[dic_index] += 1
    #print("counter list: "+str(count_arr))

    # Modify the count array such that each element at each index stores the sum of previous counts.
    i = 1
    while i < len(count_arr):
        count_arr[i] += count_arr[i - 1]
        i+=1
    #print("modified counter list: "+str(count_arr))
    
    # create the return vector
    for i in range(len(arr)):

        dic_index = dic_arr.index(arr[i])
        #print("dic index: "+str(dic_index))
        ret_index = count_arr[dic_index] - 1
        #print("ret index: "+str(ret_index))
        count_arr[dic_index] += -1
        #print("count_arr: "+str(ret_index))
        ret_arr[ret_index] = arr[i]

    return ret_arr

if __name__ == '__main__': 
    a = [1,3,7,5,34,-34,-57,65,-76,-2,1,1,-1,-1,8,0,4,3,78,3]
    sort = counting_sort(a)
    print(a)
    print(sort)