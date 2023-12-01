import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_right_angle(a, b, c):
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def main():
    try:
        x1, y1 = map(float, input("Enter the coordinates for point 1 (x1 y1): ").split())
        x2, y2 = map(float, input("Enter the coordinates for point 2 (x2 y2): ").split())
        x3, y3 = map(float, input("Enter the coordinates for point 3 (x3 y3): ").split())

        side1 = calculate_distance((x1, y1), (x2, y2))
        side2 = calculate_distance((x2, y2), (x3, y3))
        side3 = calculate_distance((x3, y3), (x1, y1))

        if is_right_angle(side1, side2, side3):
            hypotenuse = max(side1, side2, side3)
            print(f"The hypotenuse of the right-angled triangle is: {hypotenuse}")
        else:
            raise ValueError("The points do not form a right-angled triangle.")

    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()

def print_factors():
    try:
        number = input("Enter an integer: ")
        if '.' in number or not number.isdigit():
            raise ValueError("You must enter an integer.")
        else:
            number = int(number)
        print(f"The factors of {number} are:")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i)
    except ValueError as e:
        print(e)
print_factors()

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)
        if number <= 0:
            raise ValueError("The value must be a positive integer.")
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")
main()

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            raise ValueError("The number must be a positive integer greater than 0.")
        primes = get_primes(n)
        print(f"The prime numbers between 0 and {n} are: {primes}")
    except ValueError as e:
        print(f"An error occurred: {e}")
main()

def is_magic_square(square):
    magic_sum = sum(square[0])
    for row in square:
        if sum(row) != magic_sum:
            return False
    for col in range(len(square)):
        if sum(square[row][col] for row in range(len(square))) != magic_sum:
            return False

    if sum(square[i][i] for i in range(len(square))) != magic_sum:
        return False
    if sum(square[i][len(square)-1-i] for i in range(len(square))) != magic_sum:
        return False

    return True

square = []
for i in range(4):
    row = list(map(int, input("Enter row " + str(i+1) + " of the square: ").split()))
    square.append(row)

if is_magic_square(square):
    print("magic")
else:
    print("not magic")
