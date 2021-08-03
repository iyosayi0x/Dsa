# a linked list is a sequences of nodes where each node store its own data and a link to the next node 
# no preallocated space is needed ,  insertion is easier
# Functions were going to be implementing 
# insert at begining /
# insert at end /
# insert at /
# insert_values /
# insert_after_value /
# remove_by_value /
# remove_at 
# print_list /
# get_list_length /


class Node:
    def __init__(self, head=None , next=None):
        self.head = head 
        self.next = next 

class LinkedList:
    def __init__(self , head=None):
        self.head = head 
    #inserting at the start of the list
    def insert_at_begining(self , data):
        node= Node(data ,self.head)
        self.head=node
    
    #inserting at the end of the list 
    def insert_at_end(self , data):
        itr = self.head 
        if self.head is None:
            node = Node(data , self.head)
            self.head =node 
            return 
        #iterating over each item in our list 
        while itr:
            #checking if the next item is none 
            # if its none the we'll know we're at the end 
            if itr.next is None :
                #inserting a new node at the end  of the list 
                node = Node(data , None)
                itr.next = node
                break 
            itr = itr.next
            
    # inserting a fresh set of values into our list 
    def insert_values(self , data_list):
        #clearing out the head
        self.head = None 
        #looping through the items in the list and appending them to the linked list 
        for data_item in data_list :
            self.insert_at_end(data_item)
    
    def insert_at(self , index , data):
        if index < 0 or index > self.get_list_length() -1:
            raise Exception("invalid index")
        # if the index is at 0 , just insert at the begining 
        if index == 0:
            self.insert_at_begining(data)
            return 
        # else 
        count = 0
        itr = self.head
        while itr :
            if count == index - 1:
                node = Node(data , itr.next)
                itr.next= node
                break
            count +=1
            itr = itr.next
        # removing item by a value 
    def remove_by_value(self, data_name):
        itr = self.head 
        while itr :
            # when the next data_name is found replace it with what comes after it 
            if itr.next.head == data_name:
                itr.next =itr.next.next
                break 
            if itr.next is None:
                break 
            itr = itr.next
            
    def remove_at(self , index):
        if index < 0 or index > self.get_list_length() -1 :
            raise Exception("invalid index")
        if index == 0:
            itr = self.head 
            self.head = itr.next
            return
        
        count = 0 
        itr = self.head 
        while itr:
            if count == index -1 :
                # node = Node(None , itr.next)
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
            
    #inserting after a value 
    def insert_after_value(self , data_after , data_to_insert):
        itr = self.head
        while itr :
            # when the element is found 
            if itr.head == data_after:
                #create a node 
                node = Node(data_to_insert , itr.next)
                #replace the former node with the new node
                itr.next = node 
                break
            if itr.next is None :
                break
            itr = itr.next
            
    #printing out the contents of the list     
    def print_list(self):
        itr = self.head 
        if self.head is None :
            print("List is currently empty")
            return 
        list=''
        while itr :
            list += f"{itr.head} --> "
            itr = itr.next
        print(list)
    
    def get_list_length(self):
        itr = self.head
        count = 0 
        #when the next iteration item is None break the loop 
        while itr:
            count +=1 
            itr = itr.next
        return count 
    #inserting after a specified value 

            
        
li = LinkedList()
li.insert_values([i*2 for i in range(1,10)])
li.print_list()
li.insert_after_value(6 , 10)
li.remove_by_value(6)
li.insert_at_begining(20)
li.insert_at_end(20)
li.print_list()
li.remove_at(2)
li.remove_at(3)
li.remove_at(0)
li.remove_at(0)
li.print_list()
