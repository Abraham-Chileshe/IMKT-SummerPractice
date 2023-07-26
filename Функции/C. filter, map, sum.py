def is_div(number: int, filter=9):
    return number % filter == 0

def power(number: float, step=2):
    return number ** step

print(sum(map(power, (list(filter(is_div, range(10, 99 + 1)))))))

#The code uses the is_div function to filter numbers in the range 10 to 99
# that are divisible by 9. It then applies the power function to each 
# filtered number, squaring them. Finally, it calculates the sum of the squared
# numbers and prints the result.

#Output result
#40905
