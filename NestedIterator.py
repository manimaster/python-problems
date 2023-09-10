class NestedIterator:
    """
    The class initializes with a nested list.
    It uses a helper function to flatten the list recursively.
    The next() function pops the first element, and hasNext() checks if there are more elements.
    """
    def __init__(self, nestedList):
        self.list = self.flatten(nestedList)

    def flatten(self, lst):
        flat = []
        for item in lst:
            if isinstance(item, int):
                flat.append(item)
            else:
                flat.extend(self.flatten(item))
        return flat
    
    def next(self):
        return self.list.pop(0)
    
    def hasNext(self):
        return len(self.list) > 0

lst = [[1,1],2,[1,1]]
itr = NestedIterator(lst)
while itr.hasNext():
    print(itr.next())  # Outputs: 1, 1, 2, 1, 1 sequentially
