
class Stack:
    def __init__(self):
        # internal storage for my data structure
        # the _ before storage _storage denotes that the attribute should be private
        # Python does not really have the `private` keyword explicitly so this 
        # is the way to signal private methods / attrib
        # storage is not exposed to the external word, it is private / internal
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        # put something onto the stack
        self._storage.append(item)

    def pop(self):
        # remove an item from the stack
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item
