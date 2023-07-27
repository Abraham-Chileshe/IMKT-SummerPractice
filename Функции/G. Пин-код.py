def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_power_of_two(n):
    return n > 0 and (n & (n - 1) == 0)

def check_pin(pinCode):
    a, b, c = map(int, pinCode.split('-'))
    if not is_prime(a):
        return "Invalid"
    if not is_palindrome(b):
        return "Invalid"
    if not is_power_of_two(c):
        return "Invalid"
    return "Valid"

def test(pin):
    result = check_pin(pin)
    print(result)


test("7-101-4")
test("12-22-16")



