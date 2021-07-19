class Queue:
    """
    Maintain a Queue using a List
    """

    def __init__(self):
        """
        Initialize the empty queue using a Python List.  
        """
        self.queue = []

    def enqueue(self, value):
        """
        Enqueue the value provided into the queue
        """
        # Add necessary code
        self.queue.append(value)

    def dequeue(self):
        """
        Dequeue the next value and return it
        """
        if len(self.queue) <= 0:
            raise IndexError()
         
        value = self.queue[0] 
        del self.queue[0]
        return value

##################################################################
# Problems to solve
###################################################################
# 1 Initilize a new queue
queue = Queue()

# 2 Add ("Bob","Han","Max")
#   Hint: This can be used from the example problem
queue.enqueue("Bob")
queue.enqueue("Han")
queue.enqueue("Max")

# 3 Serve "Bob" using the dequeue()
print(queue.dequeue())

# 4 Add ("Joe")
queue.enqueue("Joe")

# 5 Print results clearing the queue
#   Hint: This should print Han, Max, Joe and the queue will be empty after
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

# print(queue.dequeue()) # Notice that if we pass the stored values it will print error
# This portion can be written multiple ways to achieve the same results.
