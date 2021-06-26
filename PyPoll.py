# Get data
import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total_votes variable
total_votes = 0

# Declare new list
candidate_options = []

# Declare new Dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the elections results and read file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Total number of votes cast
        total_votes += 1

        # Print the canidate name for each row
        candidate_name = row[2]

        # if the candidate is not is list then add
        if candidate_name not in candidate_options:
            # Append canidate_name to the candiate_options list
            candidate_options.append(candidate_name)
            # Begin tracking that canidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Loop candidate_options by candidate name to gather votes for the candidiate 
for candidate_name in candidate_votes: 
    # Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    #Calculate percentage of votes for candidate
    vote_percentage = (float(votes) / float(total_votes))

    # Determine winning vote count and candidate
    # Determine if votes is greater than the winning_count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes, winning_percentage = vote_percentage 
        # and winning_candidate to candidate's name.
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    # Print canditate and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1%} ({votes:,})\n")

winning_candidate_summary = (
    f"---------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1%}\n"
    f"---------------------------------------------\n")
print(winning_candidate_summary)