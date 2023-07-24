def is_palindrome(s):
    # Remove spaces from the string and convert all characters to lowercase
    s = s.replace(' ', '').lower()
    return 'YES' if s == s[::-1] else 'NO'


input_string = input()

result = is_palindrome(input_string)
print(result)