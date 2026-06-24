#general
text = "Python is the best programming language"
reversed_text = text[::-1]
print(f"First letter is ({text[0]})")
print(f"Last letter is ({text[-1]})")
print(f"Letter with index 7 ({text[7]})")
print(f"First seven symbols: {text[:7]}")
print(f"Last eight symbols: {text[-8:]}")
print(f"Reversed text: {reversed_text}")
print(f"Second symbols {text[::2]}")
#1 
def get_first_last(text):
    return text[:3], text[-3:]
last_first = get_first_last(text)

print(last_first)

#2

def reverse_str(text):
    result = ""
    for char in text:
        result = char + result
    return result

res = reverse_str(text)
print(res)

#3 
print(text[1:-1])
