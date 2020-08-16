class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k + 1
        self.front = 0
        self.rear = 0
        self.queue = [0] * self.capacity
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.front = (self.front -1 + self.capacity) % self.capacity
            self.queue[self.front] = value
            return True 
        else:return False

        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True
        else:return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return True 
        else:return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():return False
        else:
            self.rear = (self.rear -1 + self.capacity) % self.capacity
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.queue[self.front]
        else:return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.queue[(self.rear -1 + self.capacity) % self.capacity]
        else:return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.rear == self.front:
            return True
        else:return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if (self.rear + 1) % self.capacity == self.front:
            return True
        else:return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()