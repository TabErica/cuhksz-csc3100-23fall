n = int(input())
players = []
for i in range(n):
    p, h, d = input().split()
    players.append((int(p), int(h), d, i))
players.sort(reverse=True)

def battle(player, battle_list, surviver): 
    if len(battle_list) == 0:
        surviver.append(player)
    else:
        opposite = battle_list.pop()
        if opposite[1] > player[1]:
            opposite = (opposite[0], opposite[1] - 1, opposite[2], opposite[3])
            battle_list.append(opposite)
        elif opposite[1] == player[1]:
            return
        elif opposite[1] < player[1]:
            player = (player[0], player[1] - 1, player[2], player[3])
            battle(player, battle_list, surviver)


battle_list = []  
surviver = []
for player in players:
    if player[2] == 'D':
        battle_list.append(player)
    elif player[2] == 'U':
        battle(player, battle_list, surviver)

surviver += battle_list
surviver.sort(key=lambda x: x[3])

for survivor in surviver:
    print(survivor[1])