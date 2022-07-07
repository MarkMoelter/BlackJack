##### steps #####
### player information ###
# check the number of players:
# - ask for names
# - ask for bets
# - subtract bets from account total

### dealing ###
# deal a face up card and a face down card to the dealer
# deal two face up cards to each player
# - if the two cards are an ace and face
#  -- add 2.5x their bet to their account, remove from table

### player choices ###
# ask each player if they want to hit or stay:
# - if 'hit', deal another face up card to the player
# -- if over 21, they lose, remove their bet from the table
# - if 'stay', move to the next player

### decide winner ###
# after each player is finished, reveal the dealer's hidden card and hit until it exceeds 17
# - if the total is greater than 21, all remaining players
# - players remaining with totals greater than the dealer's total get 2x their bet added to account


### programming setup ###
class Cards:
    pass





# card class
# user interface class
#
#

if __name__ == "__main__":
    player = Player('Mark')
    print(player)
