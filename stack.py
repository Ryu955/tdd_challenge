class Stack():

    size = 0


    def isEmpty(self):
        return True
    
    def push(self, value):
        self.value = value
        Stack.size += 1

    def top(self):
        return self.value
    
    def size(self):
        return Stack.size
