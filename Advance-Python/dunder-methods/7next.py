""" 

=> __next__ 

    -> Control next item in iteration 
    -> iterator implement next



"""


class Counter:
    def __init__(self, limit):
        self.current = 1 
        self.limit = limit

    def __iter__(self):
        return self 

    def __next__(self):

        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

count = Counter(3)

print(next(count))

print(next(count))

print(next(count))


print(next(count))