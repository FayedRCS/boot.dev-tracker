def split_players_into_teams(players):
    
    even_team = players[0:len(players):2]
    odd_team = players[1:len(players):2]

    return even_team, odd_team


#print testing

'''test = ["player1", "player2", "player3", "player4"]

split_players_into_teams(test)'''