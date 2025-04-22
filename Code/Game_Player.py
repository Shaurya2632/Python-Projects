player_name = []

player_count = int(input("Enter player count: "))

if player_count == 0:
    print("please enter valid player count")

for i in range(player_count):
    if player_count == 0:
        break
    input_player = input(f"Enter player {i+1} name: ")
    player_name.append(input_player)

print(f"Player names: {player_name}")
