from heapq import heapify, heappop, heappush, heappushpop


class heap:
    def __init__(self, size):
        self._data = list()
        self._size = size

    def push(self, item):
        if len(self._data) < self._size:
            heappush(self._data, item)
        else:
            heappushpop(self._data, item)
    
    def get_data(self):
        return [v[1] for v in self._data]
