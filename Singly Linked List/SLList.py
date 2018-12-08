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
    
    # Returns a bool of whether or not the elem exists 
    def isExist(self, elem):
        current = self._head
        
        # traverse through the list till you either hit the end of the list or
        # the node being searched for is found
        while(current._next != None):
            # the node has been found
            if current.elem == elem:
                return True
            current = current._next
        # node has not been found
        return False
        
    def __repr__(self):
        current = self._head
        string = ''
        if self.isEmpty():
            return "The list is empty!"
        
        while(current != None):
            string += str(current.elem) + '->'
            current = current._next
        return string + "None"    
    
    # Add the new node at the head of the list
    def addFirst(self, elem):
        self._head = node(elem, self._head)
        self._size += 1
    
    # Add the new node at the end of the list
    def addLast(self, elem):
        # elem = '[{}]'.format(self._size) + elem // Future implementation that
        # shows the index along with the node
        
        # If the list is empty, new node will be added to the head
        if self.isEmpty():
            self.addFirst(elem)
        
        # The list is not empty, traverse to the end of the list then add
        # the new node
        else:
            current = self._head
            
            # traverse through the list until you hit the last node
            while(current._next != None):
                current = current._next
                
            # Assign the new node to the empty node
            current._next = node(elem, current._next)
            self._size += 1
    
    # Add the new node at a given index
    def addAtIndex(self, elem, index):
        # If the list is empty or the index is 0, add the new node to the head
        # of the list
        if self.isEmpty() or index == 0:
            self.addFirst(elem)
        
        # If the index exceeds the size of the list, relay the message and
        # return None
        elif index > self._size:
            print("Index out of range!")
            return
        
        # Traverse up to the node before the index given, then link new node
        # to the node before it and the node next to it.
        else:
            current = self._head
            count = 0
            
            # Traverse through the list
            while(current._next != None and
                  count != index - 1):
                current = current._next
            
            # current is now at the index before the given index    
            current._next = node(elem, current._next)
            self._size += 1
    
    def removeElem(self, elem):
        # If the list is empty, display it is empty and return None
        if self.isEmpty():
            print("The list is empty!")
            return
        
        # If the node to be removed is the head, re-assign the head to the node
        # next to it
        elif (self._head.elem == elem):
            self._head = self._head._next
            self._size -= 1
            return
        
        # Traverse through the list till the elem to be deleted is found then
        # remove and return it
        else:
            current = self._head
            
            # Traverse through the list
            while(current._next != None and 
                  current._next.elem != elem):
                current = current._next
        
        # traversed through the list without finding the given elem
        if current._next.elem != elem:
            print("node does not exist")
            return
        
        current._next = current._next._next
        self._size -= 1
    
    # Remove a node at a given index
    def removeAtIndex(self, index):
        # The list is empty
        if self.isEmpty():
            print("The list is empty!")
            return
        
        # Node to be removed is the head
        elif index == 0:
            self._head = self._head._next
            self._size -= 1
            return
        
        # Traverse through the list up to index - 1, then link the new node
        # to the node at index - 1 and the node at index + 1
        else:
            current = self._head
            # Count to stop while loop before the index given
            count = 0
            
            # Traverse through the list
            while(current._next != None and 
                  count != index - 1):
                current = current._next
                count += 1
                
            current._next = current._next._next
            self._size -= 1