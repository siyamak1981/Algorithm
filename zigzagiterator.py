class ZigZag:
    def __init__(self, list1, list2):
        self.queue = [list1, list2]
        # self.queue => [[1, 12, 5, 7, 9], [2, 4, 6, 8, 10]]
    
    def next(self):
        x = self.queue.pop(0)
        # print(x) #[1, 12, 5, 7, 9]
        y = x.pop(0)
        # print(x) =>[12,5,7,9]
        # print(y) => 1
        # print(self.queue)=> [[2, 4, 6, 8, 10]]
        if x:
            self.queue.append(x)
        return y
    
    def has_next(self):
        if self.queue:
            return True
        return False

z = ZigZag([1, 12, 5, 7, 9], [2, 4, 6, 8, 10])
while z.has_next():
    print(z.next(), end = " ")
    
# -------------------------------------------------


def foo(x):
    if x:
        y = x.pop(0)
        z = y.pop(0)
        if y:
            x.append(y)
        print(z, end= " ")
        foo(x)
foo([[1, 12, 5, 7, 9], [2, 4, 6, 8, 10]])


