# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)

#print(data)
# Find data type of the file
type_of_data = type(data)
print("Type of data is {0}".format(type_of_data))

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print("City in which match was played is {0}".format(city))

venue = data['info']['venue']
print("Venue of the match was {0}".format(venue))
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info']['teams']
print("teams playing in the tournament are {0} and {1}".format(teams[0],teams[1]))

no_of_teams = len(teams)
print("No. of teams that participated in the tournament is {0}".format(no_of_teams))

# Which team won the toss and what was the decision of toss winner ?
toss_winner = data['info']['toss']['winner']
print("{0} won the toss".format(toss_winner))

toss_decision = data['info']['toss']['decision']
print("{0} opted to {1} after winning the toss".format(toss_winner,toss_decision))
# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print("first bowler to bowl was {0}".format(first_bowler))

first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print("first batsman to bat was {0}".format(first_batsman))
# How many deliveries were delivered in first inning ?
no_of_deliveries_first_innings = len(data['innings'][0]['1st innings']['deliveries'])
print("No. of deliveries bowled in first innings is {}".format(no_of_deliveries_first_innings))

# How many deliveries were delivered in second inning ?
no_of_deliveries_second_innings = len(data['innings'][1]['2nd innings']['deliveries'])
print("No. of deliveries bowled in second innings is {}".format(no_of_deliveries_second_innings))
# Which team won and how ?
winner = data['info']['outcome']['winner']
print("Winner of the match was {}".format(winner))

winning_margin = data['info']['outcome']['by']['runs']
winning_type = list(data['info']['outcome']['by'])[0]
print("{0} won the match by {1} {2}".format(winner,winning_margin,winning_type))




