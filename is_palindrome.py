text = input().lower()
midl_phase = text.replace(" ", "")

def is_palindrome(midle_phase):
    result = ""
    for char in midle_phase:
        result = char + result
    if result == midle_phase:
        return True
    else: 
        return False
    
print(is_palindrome(midl_phase))