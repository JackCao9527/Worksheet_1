def fish_finder(depth1, depth2, depth3, depth4):
    if depth1 < depth2 < depth3 < depth4:
        print ("Fish rising")
    elif depth1 > depth2 > depth3 > depth4:
        print ("Fish diving")
    elif depth1 == depth2 == depth3 == depth4:
        print ("Fish at constant depth")
    else:
        print ("No fish")
depth1 = int(input("enter the value of depth1: "))
depth2 = int(input("enter the value of depth2: "))
depth3 = int(input("enter the value of depth3: "))
depth4 = int(input("enter the value of depth4: "))
fish_finder(depth1, depth2, depth3,depth4)

def football(number):
    above_40_count = 0
    team = True
    for i in range(number):
        points = int(input("Enter the points: "))
        fouls = int(input("Enter the fouls: "))
        stars = points * 5 - fouls * 3
        if stars > 40:
            above_40_count += 1
        if stars < 40:
            team = False
    print(above_40_count)
    if team:
        print('+')
    else:
        print('-')
number_of_players = int(input("Enter the number of players: "))
football(number_of_players)

def ways_to_roll_sum(m: int, n: int, target_sum: int) -> int:
    count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i + j == target_sum:
                count += 1
    return count
m = int(input("Enter m: "))
n = int(input("Enter n: "))
ways = ways_to_roll_sum(m, n, 10)
if ways == 1:
    print(f"There is {ways} way to get the sum 10.")
else:
    print(f"There are {ways} ways to get the sum 10.")
