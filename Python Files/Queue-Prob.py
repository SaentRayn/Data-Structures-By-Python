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
# 2 Add ("Bob","Han","Max")
#   Hint: This can be used from the example problem
# 3 Serve "Bob" using the dequeue()
# 4 Add ("Joe")
# 5 Print results clearing the queue
#   Hint: This should print Han, Max, Joe and the queue will be empty after