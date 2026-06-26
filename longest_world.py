text = input().strip()

def longest_world(text):
    longest_word = max(text.split(), key=len)
    return longest_word
print(longest_world(text))