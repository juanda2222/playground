


def max_length_sorted_arrays(arr1:list, arr2:list) -> int:

    total_lenth = len(arr1) + len(arr2)

    # start point:
    index1 = 0
    index2 = 0
    combined_array = list()
    median = 0

    # define the stop index:
    stop_index = int( total_lenth / 2 ) # exact center if impar number of elements, used then sum is even
    pos_low = int( total_lenth / 2 ) - 1 # lower index if a even list sum

    for i in range(total_lenth):
        
        # theck with the pointers which one is smaller
        if arr1[index1] > arr2[index2]:
            
            # print("index2: ", index2)
            # print("2 smaller: ", arr1[index1], arr2[index2])

            combined_array.append(arr2[index2])
            index2 += 1 

        elif arr1[index1] <= arr2[index2]:
            # print("index1: ", index1)
            # print("1 smaller or equal: ", arr1[index1], arr2[index2])

            combined_array.append(arr1[index1])
            index1 += 1 

        #stop using median point logic:
        if i >= stop_index:      
            print("Stoped using median point logic")   
            break

        # stop if ponter reach the end of arr1
        elif index1 == len(arr1):
            print("Stoped because arr1 ended")
            combined_array += arr2[index2:]  # concatenate the rest
            break

        # stop if ponter reach the end of arr1
        elif index2 == len(arr2):
            print("Stoped because arr2 ended")
            combined_array += arr1[index1:]  # concatenate the rest
            break

    print(combined_array)

    # make an average
    if total_lenth % 2 == 0:
        median = ( combined_array[pos_low] + combined_array[pos_low + 1] ) / 2

    # use the index:
    else:
        median = combined_array[stop_index]
       
    return median



if __name__ == "__main__":
    a = [5]
    b = [1, 4, 78, 78, 100, 111]

    result = max_length_sorted_arrays(a, b)

    print('Array a: {} Array b: {}'.format(b, a))
    print('Result: {}'.format(result))