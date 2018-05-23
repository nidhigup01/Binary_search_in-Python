# -*- coding: utf-8 -*-
"""
Created on Tue May 22 07:03:10 2018

@author: nidhi
learned from : https://www.youtube.com/watch?v=zeULw-a7Mw8
"""
list1 = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
value = 6
def binary_search_linear(list1, value):
    for i in range (len(list1)):
        if list1[i] == value:
            print('value is in the list')
            return True      
    print('value not in the list')
    return
            

def binary_search_iterative (list1, value):
    
    l = len(list1)
    while l > 0 :
        mid_index = (l-1)//2
        if len(list1) ==0 or (len(list1)==1 and list1[0]!= value):
            print ('value not in the list')
            return -1
        elif list1[mid_index] == value or list1[0]==value:
            print ('value is in the list')
            return True
        
        elif list1[mid_index] < value:  
            list1 = list1[mid_index+1:]
            print ('first mid_index', mid_index)
            print('truncated first list1', list1)
            l = len(list1)
        elif list1[mid_index] > value:
            list1 = list1[:mid_index-1]
            print ('second mid_index', mid_index)
            print('truncated second list1', list1)
            l = len(list1)
               
    return False
def binary_searchiterativeindex(list1, value):
    low = 0
    high = len(list1)-1
    
    while low <= high:
        mid_index = (low + high)//2
        if len(list1) ==0 or (len(list1)==1 and list1[0]!= value):
            
            return -1 
        elif list1[mid_index] ==value:
            print(mid_index)
            return True
        elif list1[mid_index] < value:
            low = mid_index + 1
            
        elif list1[mid_index] > value:
           
            high = mid_index-1
            
    return -1


def binary_search_recursive(list1, value):
    l= len(list1)
    mid_index = (l-1)//2
    if len(list1) ==0 or (len(list1)==1 and list1[0]!= value):
            print ('value not in the list')
            return -1 
    elif list1[mid_index] == value or list1[0]==value:
        print('value is in the list')
        return True
    elif list1[mid_index] < value:
        list1 = list1[mid_index+1:]
        binary_search_recursive(list1, value)
    elif list1[mid_index] > value:
        list1 = list1[:mid_index-1]
        binary_search_recursive(list1, value)
    
    return False
    
        
        
    
def binary_search_iteration (list1, value):
    
                
binary_search_linear(list1, 5)
binary_search_iterative(list1, 16)
binary_search_recursive(list1, 1)
  
