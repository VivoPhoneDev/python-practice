text = input().lower().replace(" ", "")


def remove_duplicates(text):
    seen = set()
    result = ""

    for char in text:
        if char not in seen:
            seen.add(char)
            result = result + char
    return result

print(remove_duplicates(text))