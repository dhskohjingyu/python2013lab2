def count_votes():
    # Open VOTES.DAT

    votes = {'PAP':0, 'RP':0, 'SDA':0, 'WP':0, 'SPOILT':0}

    try:
        infile = open("VOTES.DAT", "r")

        for line in infile:
            # remove newline from line
            line = line.rstrip('\n')
            # check if line is valid
            if line == 'PAP,1' or line == 'RP,1' or line == 'SDA,1' or line == 'WP,1':
                # Get the party name by removing the last two characters (i.e. ,1)
                party_name = line[0:-2]

                # Increment vote for that party
                votes[party_name] += 1
            else:
                # if it isn't valid, add it to spoilt votes
                votes['SPOILT'] += 1
                
        infile.close()

        return votes
    except:
        print("VOTES.DAT not found or could not be open")

def count_percentage(votes):
    # votes is a dictionary containing each party's name and their respective votes
    total_votes = 0

    # Loop through all parties
    for key in votes:
        # add vote count to total votes
        total_votes += votes[key]
        
    percentage = {}

    # Loop through all parties (and spoilt votes)
    for key in votes:
        # Find percentage for current party and add it to the dictionary
        vote_count = votes[key]
        party_percentage = float(vote_count)/float(total_votes) * 100
        percentage[key] = party_percentage
    
    return percentage

# get votes dictionary
#votes = count_votes()
# count percentage of votes
#count_percentage(votes)
