from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
        return value

    def dequeue(self):
        return self.queue.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError

        return self.queue[index]
