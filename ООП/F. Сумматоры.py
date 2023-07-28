from abc import abstractmethod

class Adders:
    list_sum = [1]

    def transform(self, num: int) -> int:
        return num

    @abstractmethod
    def sum(self, end_num: int):
        if end_num <= len(self.list_sum):
            return self.list_sum[end_num - 1]
        cur_value = self.transform(end_num) + self.sum(end_num - 1)
        self.list_sum.append(cur_value)
        return cur_value

class SquareAdder(Adders):
    list_sum = [1]
    def transform(self, num: int) -> int:
        return num ** 2

class CubeAdder(Adders):
    list_sum = [1]

    def transform(self, num: int) -> int:
        return num ** 3

def example():
    print(Adders().sum(2))  # 3
    print(Adders().sum(4))  # 10
    print(Adders().sum(6))  # 21

    print("---------------------------------")

    print(SquareAdder().sum(2))  # 5
    print(SquareAdder().sum(4))  # 30
    print(SquareAdder().sum(6))  # 91

    print("---------------------------------")

    print(CubeAdder().sum(5))  # 225
    print(CubeAdder().sum(4))  # 100
    print(CubeAdder().sum(7))  # 784


example()
