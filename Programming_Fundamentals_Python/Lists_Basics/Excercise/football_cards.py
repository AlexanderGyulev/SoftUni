sequence_of_cards = input().split()

team_a_cards = []
team_b_cards = []

terminated_flag = False

for cards in sequence_of_cards:
    if "B-" in cards:
        if cards not in team_b_cards:
            team_b_cards.append(cards)
    elif "A-" in cards:
        if cards not in team_a_cards:
            team_a_cards.append(cards)

    players_left_a = 11 - len(team_a_cards)
    players_left_b = 11 - len(team_b_cards)
    if players_left_a < 7 or players_left_b < 7:
        terminated_flag = True
        break

print(f'Team A - {players_left_a}; Team B - {players_left_b}')
if terminated_flag:
    print("Game was terminated")