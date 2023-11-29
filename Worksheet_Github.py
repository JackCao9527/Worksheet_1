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

def can_rotate(word):
    rotatable_letters = set('IOSHZXN')
    for letter in word:
        if letter not in rotatable_letters:
            return 'NO'
    return 'YES'

word = input("Enter a word: ")
print(can_rotate(word))

def balloon_touch_ground(h, M):
    for t in range(1, M+1):
        A = -6*(t**4) + h*(t**3) + 3*(t**2) + t
        if A <= 0:
            return f"The balloon first touches ground at hour: {t}"
    return "The balloon does not touch ground in the given time."

h = int(input("Enter the value: "))
M = int(input("Enter the value: "))
print(balloon_touch_ground(h, M))


