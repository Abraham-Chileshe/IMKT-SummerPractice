def knock_down_pins(N, K, throws):
    pins = ['I'] * N  # Creating a list of N pins, all standing

    for i in range(K):
        left, right = throws[i]  # We get a pair of numbers li, ri for the current roll
        for j in range(left - 1, right):  # Indexes start from 0, and the numbering of pins starts from 1, so we reduce left by 1
            pins[j] = '.'  # Update the state of the pins in the specified range to "."

    return ''.join(pins)  # Combine the list of pins into one line and return the result


N, K = map(int, input().split())  # Number of pins and number of throws
throws = [tuple(map(int, input().split())) for _ in range(K)]  # Считываем K пар чисел (li, ri)

result = knock_down_pins(N, K, throws)
print(result)