# Assumptions:
# total number of votes is 33,281
# (number of electoral votes in General Election 2012)

import random

# Constants
PUNGGOL_EAST_VOTER_COUNT = 33281

PAP_CHANCE = 48
RP_CHANCE = 5
SDA_CHANCE = 5
WP_CHANCE = 40

def generate_vote():
    '''
    Generate a vote with the following chances for the parties:
    PAP - 48% (PAP,1)
    RP - 5% (RP,1)
    SDA - 5% (SDA,1)
    WP - 40% (WP,1)
    Spoilt votes - whatever left (2% in this case)
    '''

    random_number = random.randint(0, 100)
    vote_record = ""

    if(random_number >= 0 and random_number < PAP_CHANCE):
        # Generate vote for PAP
        vote_record = "PAP,1"
    elif(random_number >= PAP_CHANCE and random_number < PAP_CHANCE + RP_CHANCE):
        # Generate vote for RP
        vote_record = "RP,1"
    elif(random_number >= PAP_CHANCE + RP_CHANCE and random_number < PAP_CHANCE + RP_CHANCE + SDA_CHANCE):
        # Generate vote for SDA
        vote_record = "SDA,1"
    elif(random_number >= PAP_CHANCE + RP_CHANCE + SDA_CHANCE and random_number < PAP_CHANCE + RP_CHANCE + SDA_CHANCE + WP_CHANCE):
        # Generate vote for WP
        vote_record = "WP,1"
    else:
        # Spoilt
        random_spoilt_number = random.randint(0, 4)

        if(random_spoilt_number == 0):
            # Invalid vote for PAP
            vote_record = "PAP,0"
        elif(random_spoilt_number == 1):
            # Invalid vote for RP
            vote_record = "RP,0"
        elif(random_spoilt_number == 2):
            # Invalid vote for SDA
            vote_record = "SDA,0"
        else:
            # Invalid vote for WP
            vote_record = "WP,0"

    return vote_record

def start_punggol_east_election():
    ''' Generate a vote for each Punggol East voter '''

    # Append them to a list
    votes = []
    for i in range(0, PUNGGOL_EAST_VOTER_COUNT):
        votes.append(generate_vote())

    # Write votes to VOTES.DAT
    try:
        outfile = open("VOTES.DAT", "w")
        
        for vote in votes:
            outfile.write(vote + "\n")
            
        outfile.close()
    except:
        print("Could not write to VOTES.DAT")

# Start the election
start_punggol_east_election()
