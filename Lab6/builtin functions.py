#1
import math

def multiply_list(numbers):
    try:
        result = math.prod(numbers)
        print(f"Product of all numbers in the list: {result}")
        return result
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    multiply_list(numbers)

#2
def count_case(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    
    print(f"Number of uppercase letters: {uppercase_count}")
    print(f"Number of lowercase letters: {lowercase_count}f")

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    count_case(input_string)

#3
def check_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()  
    return s == s[::-1]

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if check_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

#4
import time
import math

def delayed_square_root(number, delay):
    try:
        number = float(number)
        delay = int(delay) / 1000  

        print(f"Waiting for {delay * 1000} milliseconds...")
        time.sleep(delay)  

        result = math.sqrt(number)
        print(f"Square root of {number} after {delay * 1000} milliseconds is {result:.6f}")
    except ValueError:
        print("Error! Please enter a valid number")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    number = float(input("Enter a number: "))
    milliseconds = int(input("Enter milliseconds: "))
    delayed_square_root(number, milliseconds)
#5
  def all_elements_true(t):
    return all(t)

if __name__ == "__main__":
    elements = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
    print("All elements are True:", all_elements_true(elements))
 
