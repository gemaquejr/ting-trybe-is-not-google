from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

# Referencia://stackoverflow.com/questions/31874952/how-to-raise-an-indexerror-when-slice-indices-are-out-of-range
    def search(self, index):
        if index < 0 or index > len(self.queue):
            raise IndexError('list index out of range')
        return self.queue[index]
