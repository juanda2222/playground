
def get_first_non_repeated_char(string:str  = "sdfsdgbfs") -> int:
    
    keep_searching_flag = True
    i = 0

    # loop through all the characters
    while keep_searching_flag:

        if i >= len(string):  # conditional asigment to avoid overflow, no character found
            raise ValueError("unique char not found")
        
        keep_searching_flag = False
        #print("searching for: '"+string[i]+"'")

        for k, current_char in enumerate(list(string)):

            #it is repeated
            if string[i] == current_char and i != k: # diferent indexes same letter
                #print("ups its repeated")
                keep_searching_flag = True
                break
    
        i+=1

    return i-1



if __name__ == '__main__': 

    a = "sdffhhfo22r2sdworw2"
    i = get_first_non_repeated_char(a)
    print(a)
    print("the index is: "+str(i)+" and the char is: "+str(a[i]))

