

from time import sleep
from random import randint
from datetime import datetime

# open in "a" mode is the fastest option because it does not waste time reading the file.
# and we should use the "with" context only at the begining to avoid precious time delays
with open('innovators.csv', 'a') as opened_file:


    # the touple is the fastest reading object
    # so we use it to pass to the writing function:
    def append_to_file(file: type(open), row:tuple):
        
        # using this format:
        # [bandymas,"Clockwise",timestamp,accX,accY,accZ]
        #file.write("%i,%s,%s,%i,%i,%i;\n" % row ) # csv is not standarized yet so this format could work on some computers
        file.write("%i;%s;%s;%i;%i;%i,\n" % row ) # this is compatible with excel

    # this would be the time precious operation
    while True:
        
        #get the values from a sensor (in this case we are simulating them):
        now = datetime.now() # current date and time
        row = (randint(-20, 100), "Clockwise",  str(now), randint(50, 180), randint(100, 200), randint(10, 60))

        #save the row to the file
        append_to_file(opened_file, row)
        sleep(1)