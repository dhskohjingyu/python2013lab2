import datetime
import count_votes

def get_winner(votes_dictionary):
    # find highest number of votes by a party
    highest = 0
    highest_name = ""
    for key in votes_dictionary:
        votes = votes_dictionary[key]

        if(votes > highest):
            highest = votes
            highest_name = key

    return highest_name

# get current time
now = datetime.datetime.now()

date_string = now.strftime("%d/%m/%Y")

# format time
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
am_pm_string = "AM"

if(hour > 12):
    am_pm_string = "PM"
    hour -= 12
else:
    am_pm_string = "AM"

print_order = ["PAP", "RP", "SDA", "WP", "SPOILT"]
print_index = 0

# Output header
output = ""

time_string = (str(hour) + ":" + str(minute) + " " + am_pm_string)
time_whitespace = " " * (40 - len(time_string))
output += (date_string + time_whitespace + time_string) + "\n"
output += ("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION") + "\n"
output += ("WARD                PARTY     #VOTES    %VOTES") + "\n"
output += ("--------------------------------------------------") + "\n"

# get vote dictionaries
votes = count_votes.count_votes()
votes_percentage = count_votes.count_percentage(votes)

party_name = print_order[print_index]
party_name_whitespace = (3 - len(party_name) + 8) * " "
votes_whitespace = (6 - len(str(votes[party_name])) + 4) * " "
output += ("PUNGGOL EAST SMC    " + party_name + party_name_whitespace + str(votes[party_name]) + votes_whitespace + str("%0.2f" % votes_percentage[party_name])) + "\n"
print_index += 1

# print for the other 3 parties
for i in range(3):
    party_name = print_order[print_index]
    # find whitespace to properly format the string
    party_name_whitespace = (3 - len(party_name) + 8) * " "
    votes_whitespace = (6 - len(str(votes[party_name])) + 4) * " "
    output += "                    " + party_name + party_name_whitespace + str(votes[party_name]) + votes_whitespace + str("%0.2f" % votes_percentage[party_name]) + "\n"
    print_index += 1

output += "--------------------------------------------------" + "\n"

# get winner for election
winner_name = get_winner(votes)
total_votes = 0

# find total votes
for key in votes:
    total_votes += votes[key]

output += "WINNER: " + winner_name + "\n"
output += "TOTAL VOTES: " + str(total_votes) + "\n"
output += "#SPOILT VOTES: " + str(votes["SPOILT"]) + "\n"
output += "%SPOLIT VOTES: " + str("%0.2f" % votes_percentage["SPOILT"]) + "\n"

print(output)
