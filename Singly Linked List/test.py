from SLList import *

def main():
    test_list = SLList()
    
    test_list.add('First')
    test_list.add('Second')
    test_list.add('Third')
    
    test_list.remove('Second')
    
    print(test_list)
    
if __name__ == '__main__':
    main()
    