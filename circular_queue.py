import os 
class CircularQueue:
    def __init__(self, max_size):
        self.queue = {}
        self.max_size = max_size
        self.start = 0
        self.end = 0
        self.size = 0

    def enqueue(self, item):
        # If the queue is full, remove the oldest item
        if self.size == self.max_size:
            del self.queue[self.start]
            self.start = (self.start + 1) % self.max_size
        else:
            self.size += 1

        # Add the new item at the end position
        self.queue[self.end] = item
        self.end = (self.end + 1) % self.max_size

    def get_queue(self):
        # Return queue elements in order from start to end
        result = []
        i = self.start
        for _ in range(self.size):
            result.append(self.queue[i])
            i = (i + 1) % self.max_size
        return result


def circular_queues():
    queue_input_file_path = os.path.join("ust-python\input_data", "circular_queue_input.txt")
    # Read commands from the input file and execute them
    with open(queue_input_file_path, "r") as file:
        for line in file:
            nums = line.strip().split()
            cq = CircularQueue(5)
            for i in nums:
                cq.enqueue(i)  
            print(f"Input : {nums}")  
            print("Output :",list(cq.queue.values()))
            print()