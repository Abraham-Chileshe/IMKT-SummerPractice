def gematria(word):
    word = word.upper()

    # Calculating the gematria for the word
    return sum(ord(letter) - ord('A') + 1 for letter in word)

# We read the words and calculate its gematria for each word
words = []
while True:
    word = input().strip()
    if not word:
        break
    words.append(word)

# Sort the words by their gematria in ascending order, and with equal gematria — in alphabetical order
sorted_words = sorted(words, key=lambda x: (gematria(x), x))

# Output the words in the required order
for word in sorted_words:
    print(word)
