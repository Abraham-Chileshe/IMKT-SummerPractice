numbers = list(map(int, input().split()))

# List expression for getting all even elements
even_numbers = [num for num in numbers if num % 2 == 0]
print(*even_numbers)

'''
for num in numbers:
    if num % 2 == 0:
        print(num)
'''