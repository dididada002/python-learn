# 迭代器
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")

class TestIter:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = TestIter()
myIter = iter(myClass)

for x in myIter:
    print(x, end=" ")