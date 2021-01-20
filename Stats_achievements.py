def playerachievements(player_achievements, ownedgames):
    for player_games in player_achievements:
        for AM in player_games['playerstats']['achievements']:
            if AM['description'] == '':
                AM['description'] = 'No description available'


if __name__ == '__main__':
    playerachievements()