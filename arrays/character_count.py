
def character_count(string:str  = "sdfsdgbfs", char:str = "s" )-> int:
    counter = 0
    for current_char in list(string):
        if char == current_char:
            counter+=1
    return counter



if __name__ == '__main__': 

    a = "sdffhfo2r2sdw2"
    character = "f"
    n = character_count(a, character)
    print(a)
    print("number of "+character+" is: "+str(n))

