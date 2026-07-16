class AlphabetIterator():
    def __iter__(self):
        self.ch = 97
        return self
    
    def __next__(self):
        if self.ch <= 122:
            char = chr(self.ch)
            self.ch += 1
            return char
        raise StopIteration
    
for x in AlphabetIterator():
    print(x)