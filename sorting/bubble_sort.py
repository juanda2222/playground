
def bubble_sort( arr:list  = [4,8,3,6,23,90,2] ):
    if len(arr)<=0 : raise ValueError("Array too small")

    keep_looping = True
    ret_arr = list(arr)

    while keep_looping:
        
        keep_looping = False # start false to exit by default

        for i, item in enumerate(ret_arr):
            
            if i >= len(ret_arr) - 1:
                # we r already on the last item so no need to sort
                break

            elif item <= ret_arr[i+1]:
                #do nothing
                pass

            elif item > ret_arr[i+1]:
                #reverse the order
                aux = ret_arr[i]
                ret_arr[i] = ret_arr[i+1]
                ret_arr[i+1] = aux

                keep_looping = True # if at least one item if sorted check again

                
    
    return ret_arr

if __name__ == '__main__': 
    a = [1,3,7,5,2,8,0,4,3,78,3]
    sorted = bubble_sort(a)
    print(a)
    print(sorted)

