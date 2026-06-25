def count_letters(words): 
    count = {}
    for char in words:
        if char in dict:
            count[char] += 1
        else:
            count[char] = 1
    return count

words = input()
print(count_letters(words))

    