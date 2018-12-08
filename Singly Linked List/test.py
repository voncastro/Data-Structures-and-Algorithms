from SLList import *

def main():
    test_list = SLList()
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("------------------------------ADD FIRST------------------------------")
    print("addFirst called to the following nodes (in-order):\n\
    'Four', 'Three', 'Two', 'One', 'Zero'")
    
    test_list.addFirst('Four')
    test_list.addFirst('Three')
    test_list.addFirst('Two')
    test_list.addFirst('One')
    test_list.addFirst('Zero')
    print()
    print("Single Linked List is now:",test_list)
    print("------------------------------END ADD FIRST--------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("------------------------------ADD LAST-------------------------------")
    print("addLast called to the following nodes (in-order):\n\
    'Five', 'Six', 'Seven', 'Eight', 'Nine'")
    
    test_list.addLast('Five')
    test_list.addLast('Six')
    test_list.addLast('Seven')
    test_list.addLast('Eight')
    test_list.addLast('Nine')
    print()
    print("Single Linked List is now:",test_list)
    print("------------------------------END ADD LAST---------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    
if __name__ == '__main__':
    main()
    