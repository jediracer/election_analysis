# Get data
import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)   


    # Print each row in the CSV file.
   # for row in file_reader:
    #    print(row)



# 1. Total number of votes cast
# 2. List of candidates who received votes
# 3. Percentage of votes each candidate received
# 4. Total number of votes each candidate received
# 5. The winner of the election based on popular vote
# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
##with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     ##txt_file.write("Counties in the Election\n")
     ##txt_file.write("-------------------------\n")
     ##txt_file.write("Arapahoe\nDenver\nJefferson\n")