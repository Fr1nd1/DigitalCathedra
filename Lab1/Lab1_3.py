list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_players = len(list_players)
count_of_players_in_one_team = count_of_players // 2
team1 = list_players[:count_of_players_in_one_team]
team2 = list_players[count_of_players_in_one_team:]

print(team1)
print(team2)