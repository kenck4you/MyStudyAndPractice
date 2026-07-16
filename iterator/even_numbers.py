class EvenNumbers():
    
    def __iter__(self):
        self.c = 1
        self.a = 2
        return self
    
    def __next__(self):
        if self.c > 10:
            raise StopIteration
        value = self.a
        self.a += 2
        self.c += 1
        return value
    
for x in EvenNumbers():
    print(x)