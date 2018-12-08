from node import *
from test import *

class SLList:
    def __init__(self):
        self._head = None
        self._size = 0
     
     
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return len(self) == 0
    
    
    def add(self, elem):
        elem = '[{}]'.format(self._size - 1) + elem
        # If the list is empty, new node will be added to the head
        if self.isEmpty():
            self._head = node(elem, None)
            self._size += 1
        
        else:
            current = self._head
            
            # traverse through the list until you hit the last node
            while(current._next != None):
                current = current._next
                
            # Assign the new element to the empty node
            current._next = node(elem, current._next)
    
    def remove(self, elem):
        # If the list is empty, display it is empty and return None
        if self.isEmpty():
            print("The list is empty!")
            return
        
        # The
        # Traverse through the list till the elem to be deleted is found then
        # remove and return it
        else:
            current = self._head
            while(current._next.elem != elem and 
                  current._next != None):
                current = current._next
        
        if current._next == None:
            print("Element does not exist")
            return
        
        current._next = current._next._next
        self._size -= 1
        
    def __repr__(self):
        current = self._head
        string = ''
        
        while(current != None):
            string += str(current.elem) + '->'
            current = current._next
        return string + "None"
    
if __name__ == '__main__':
    print("Running from SLList.py")
    