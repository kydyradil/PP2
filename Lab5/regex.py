#1
import re

def match_pattern(text):
    pattern = r'^ab*$'  
    return bool(re.fullmatch(pattern, text))


user_input = input("Enter a string: ")
print("Match found" if match_pattern(user_input) else "No match found")


    #2
import re

def match_pattern(text):
    pattern = r'^ab{2,3}$' 
    return bool(re.fullmatch(pattern, text))


user_input = input("Enter a string: ")
print("Match found" if match_pattern(user_input) else "No match found")


#3
import re

def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'  
    return re.findall(pattern, text)


user_input = input("Enter a string: ")
matches = find_sequences(user_input)

print("Found sequences:", matches if matches else "No matches found")

#4
import re

def find_sequences(text):
    pattern = r'\b[A-Z][a-z]+\b'  
    return re.findall(pattern, text)

user_input = input("Enter a string: ")
matches = find_sequences(user_input)

print("Found sequences:", matches if matches else "No matches found")

#5
import re

def match_pattern(text):
    pattern = r'^a.*b$'  
    return bool(re.fullmatch(pattern, text))

user_input = input("Enter a string: ")
print("Match found" if match_pattern(user_input) else "No match found")

#6
import re

def replace_chars(text):
    pattern = r'[ ,.]'  
    return re.sub(pattern, ':', text)

user_input = input("Enter a string: ")
print("Modified string:", replace_chars(user_input))

#7 
import re

def snake_to_camel(text):
    words = text.split('_')  
    return words[0] + ''.join(word.capitalize() for word in words[1:])

user_input = input("Enter a snake_case string: ")
print("CamelCase string:", snake_to_camel(user_input))

#8 
import re 

def split_at_uppercase(text):
    return re.split(r'(?=[A-Z])', text)

user_input = input("Enter a string: ")
print("Split string:", split_at_uppercase(user_input))

#9 
import re

def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

user_input = input("Enter a string: ")
print("Modified string:", insert_spaces(user_input))

#10 
import re

def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

user_input = input("Enter a CamelCase string: ")
print("snake_case string:", camel_to_snake(user_input))





