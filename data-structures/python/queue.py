# Queues is a data structure which is similar to stacks 
# It follows a FILO behaviour -> First In Last Out 
# elements are inserted from one end called the rear and deleted from the other end called the front

#lets implement a Queue
class Queue:
    def __init__(self):
        self.queue = []
    #adding an item to a queue is called enqueue 
    def enqueue(self , new_item):
        self.queue.insert(0 , new_item)
    #removing an item from a queue is called dequeue 
    def dequeue(self):
        return self.queue.pop()
    #checking if the queue is empty 
    def is_empty(self):
        return self.queue == []
    #printing out the queue 
    def print_queue(self):
        print(self.queue)
    
#create an instance of our queue class
queue = Queue()
queue.enqueue("queue")
queue.enqueue("front")
queue.print_queue()

#lets empty our queue 
while True:
    item = queue.dequeue()
    print(f"Removed {item}")
    if queue.is_empty():
        break

queue.print_queue()