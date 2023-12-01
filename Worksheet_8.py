def mood_detector(message):
    happy = message.count(':-)')
    sad = message.count(':-(')

    if happy == 0 and sad == 0:
        return 'none'
    elif happy == sad:
        return 'unsure'
    elif happy > sad:
        return 'happy'
    else:
        return 'sad'

messages = input("Enter your messages:")
print(mood_detector(messages))

def count_votes():
    V = int(input("Enter the total number of votes: "))
    votes = input("Enter the sequence of votes: ")

    A_votes = votes.count('A')
    B_votes = votes.count('B')

    if A_votes > B_votes:
        return 'A'
    elif B_votes > A_votes:
        return 'B'
    else:
        return 'Tie'

print(count_votes())

def can_use_on_sign(word):
    allowed_letters = set("IOSHZXN")
    return all(letter in allowed_letters for letter in word)
word = input("Enter the word in uppercase letters: ").strip()
if can_use_on_sign(word):
    print("YES")
else:
    print("NO")

def find_balloon_touchdown(humidity, max_hours):
    for t in range(1, max_hours + 1):
        altitude = -6 * (t ** 4) + humidity * (t ** 3) + 3 * (t ** 2) + t
        if altitude <= 0:
            return t
    return None
h = int(input("Enter the humidity factor (0-100): "))
M = int(input("Enter the maximum number of hours Margaret will wait: "))
touchdown_hour = find_balloon_touchdown(h, M)
if touchdown_hour is None:
    print("The balloon does not touch ground in the given time.")
else:
    print(f"The balloon first touches ground at hour: {touchdown_hour}")
