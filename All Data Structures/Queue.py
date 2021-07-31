class queue:
    def __init__(self,data):
        self.queue=[data]

    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if(self.queue):
            print(f"{self.queue.pop(0)} removed")
    def size(self):
        return self.queue

    def display(self):
        print(self.queue)