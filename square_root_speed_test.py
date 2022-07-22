#This code determinates 3 differents methods to calculate a square root of a list, and returns the times taked with each method. 

import time
import math

the_list = []
for i in range(0,10000000):
    the_list.append(i)
the_list2 = []
#print (the_list)

def method1():
    #getting the start time
    st = time.time()
    for item in the_list:
        the_list2.append(math.sqrt(item))
        #print(the_list2)
    #getting the elapsed time
    et = time.time()
    elapsed_time= et - st
    return elapsed_time

def method2():
    the_list2.clear()
    st = time.time()
    for item in the_list:
        the_list2.append(pow(item,0.5))
    et = time.time()
    elapsed_time= et - st
    return elapsed_time

def run():
    first_test = method1()
    first_test= round(first_test,4)
    print ("Executing First test..\n")
    print(first_test, " seconds taked in the first method.\n")
    second_test = method2()
    second_test=round(second_test,4)
    print(" Executing Second test...\n")
    print(second_test, "elapsed during second method.")

# Conclussion : Usually the second method has proved to be faster , 30% faster usually.



if __name__ == "__main__":
    run()

