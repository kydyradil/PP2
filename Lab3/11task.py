def is_palindrome(text):
    text = text.replace(" ", "").lower()  
    return text == text[::-1]


word = input(" ")


if is_palindrome((word)):
    print("YES!")
else:
    print("NO!")