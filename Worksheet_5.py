x = 10
def foo():
    x = 20
    y = 12
print(x)

user_input = input("Enter a string: ")
first_two_chars = ''
for char in user_input:
    if len(first_two_chars) < 2:
        first_two_chars += char
print(first_two_chars)

name = input("Please enter a name: ")
capitalises_name = name.capitalize()
print(capitalises_name)

user_input = input("Enter a string: ")
contains_digit = any(char.isdigit() for char in user_input)
print(contains_digit)

def is_valid_password(password):
  if len(password) <= 8:
    return False
  if not all (x.isalnum() for x in password):
    return False
  if all (x.isdigit() for x in password) and all(x. isalpha() for x in password):
    return False
  return True
password = input("Please enter a password: ")
print (is_valid_password(password))

ascii_code = int(input("Enter an ASCII code: "))
if 0 <= ascii_code <= 127:
    character = chr(ascii_code)
    print("The character is", character)
else:
    print("Invalid input. Please enter a number between 0 and 127.")

def count_letters(string):
    count = 0
    for ch in string:
        if ch.isalpha():
            count += 1
    return count
string = input("Enter a string: ")
print("The number of letters in the string is:", count_letters(string))

def get_row_column(cell: str) -> (int, int):
    column = int(cell[1:]) - 1
    row = ord(cell[0].upper()) - ord('A')
    return row, column
user_input = input("Please enter a cell: ")
row, column = get_row_column(user_input)
print("Row:", row)
print("Column:", column)

def encrypt_message(n: int, message: str) -> str:
    encrypted = ""
    for char in message:
        if 'a' <= char <= 'z':
            shift = (ord(char) - ord('a') + n) % 26
            encrypted += chr(shift + ord('a'))
        elif 'A' <= char <= 'Z':
            shift = (ord(char) - ord('A') + n) % 26
            encrypted += chr(shift + ord('A'))
        else:
            encrypted += char
    return encrypted
n = int(input("Enter the integer n: "))
message = input("Enter your message: ")
encrypted_message = encrypt_message(n, message)
print(f"Encrypted message: {encrypted_message}")
