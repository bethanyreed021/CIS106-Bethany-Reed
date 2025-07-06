def comp_batting_avg(num_of_hits,num_of_bats):
    batting_avg = num_of_hits / num_of_bats
    return batting_avg

num_of_players = 0

response = input("Do you want to start this program (Yes or No)?")

while(response == 'Yes'):
    last_name = input("Enter last name: ")
    num_of_hits = int(input("Enter number of hits: "))
    num_of_bats = int(input("Enter number of bats: "))
    batting_avg = comp_batting_avg(num_of_hits,num_of_bats)
    print("Last name: ", last_name)
    print("Batting average: ", batting_avg)
    num_of_players = num_of_players + 1
    response = input("Do you want to continue this program (Yes or No)?")

print("Number of players: ", num_of_players)