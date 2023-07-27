class Balance:
    def __init__(self, left_weight: float = 0, right_weight: float = 0):
        self.left = left_weight
        self.right = right_weight

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left > self.right:
            return "L"
        elif self.left < self.right:
            return "R"
        return "="


def example1():
    balance = Balance(0, 0)
    balance.add_right(10)
    balance.add_left(9)
    balance.add_left(2)
    print(balance.result())

def example2():
    balance = Balance(0, 0)
    balance.add_right(10)
    balance.add_left(5)
    balance.add_left(5)
    print(balance.result())
    balance.add_left(1)
    print(balance.result())


example1()
print("-----------------------")
example2()
