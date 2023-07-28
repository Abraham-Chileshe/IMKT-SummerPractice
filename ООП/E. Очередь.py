from __future__ import annotations

class Queue:
    def __init__(self, *values: list[int | float | str] | int | float | str):
        if len(values) == 0:
            raise ValueError("Number of elements = 0")
        if isinstance(values[0], list):
            self.q = values[0]
        else:
            self.q = list(values)

    def append(self, *values: int | float | str):
        if len(values) == 0:
            raise ValueError("Number of elements = 0")
        self.q.extend(values)

    def copy(self):
        return Queue(self.q.copy())

    def pop(self) -> int | float | str | None:
        try:
            value = self.q[0]
            rem_first(self.q)
            return value
        except:
            return None

    def extend(self, other: "Queue"):
        self.q.extend(other.q)

    def next(self):
        try:
            a = self.q.copy()
            rem_first(a)
            return Queue(a)
        except:
            return None

    def __add__(self, other):
        a = self.q.copy()
        a.extend(other.q)
        return Queue(a)

    def __iadd__(self, other):
        self.extend(other) #same as +=
        return self

    def __eq__(self, other):
        return self.q == other.q

    def __rshift__(self, other):
        a = self.q.copy()
        for _ in range(other):
            rem_first(a)
        return Queue(a)

    def __str__(self) -> str:
        return "[" + "->".join(str(element) for element in self.q) + "]"


def rem_first(a: list):
    a.remove(a[0])


def next(other: "Queue"):
    try:
        a = other.q.copy()
        rem_first(a)
        return Queue(a)
    except:
        return None


def example1():
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    qx = q1.copy()
    print(qx.pop())
    print(qx)
    q2 = q1.copy()
    print(q2)
    print(q1 == q2, id(q1) == id(q2))
    q3 = q2.next()
    print(q1, q2, q3, sep='\n')
    print(q1 + q3)
    q3.extend(Queue(1, 2))
    print(q3)
    q4 = Queue(1, 2)
    q4 += q3 >> 4
    print(q4)
    q5 = next(q4) 
    print(q4)
    print(q5)


example1()
