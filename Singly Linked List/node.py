class node:
    def __init__(self, elem, next):
        self.elem = elem
        self._next = next
        
        def __repr__(self):
            return self.elem