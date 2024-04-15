#!/usr/bin/env python3

'''
This is the final exam. Leggo
Creator: rbondoc1
'''
import sys
#import os

def fileop(file_name: str):
    try:
        file = open(file_name,'r')
        file_content = file.read()
        file.close()
        return file_content
    
    except FileNotFoundError:
        return ''
        
    
def process_data(xlist: list):

    counter = 0
    for x in xlist:
        if x == 'banana':
            counter = counter + 1
    return counter

if __name__ == "__main__":

    arguments = sys.argv
    arg_num = len(arguments)
#    print(arguments)
    if arg_num > 1:
        
        for arg in arguments[1:]:
            x = fileop(arg)
            x_list = x.split()

            banana_num = process_data(x_list)
            
            print(f"{arguments[0]}: {banana_num} bananas!")

    else:
        print("Error: no arguments found")
        


        
    

'''
    x = fileop("test.file")
    x_list = x.split()
    #print(x_list)

    banana_num = process_data(x_list)
    print(banana_num)
'''

