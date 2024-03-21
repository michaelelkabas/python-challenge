import csv

# Path to the election data CSV file
election_data_csv = "Resources/election_data.csv"

# Initialize variables for election analysis separately to keep the code orginized and simple to understand 
total_votes_count = 0
candidate_votes_count = {}
election_winner = ""
winner_votes_count = 0

# Read the CSV file for election analysis
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)

    # Loop through each row in the CSV file for election analysis
    for row in csvreader:
        # Increment total votes
        total_votes_count += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # Add candidate to the dictionary if not already present
        if candidate_name not in candidate_votes_count:
            candidate_votes_count[candidate_name] = 0

        # Increment candidate's vote count
        candidate_votes_count[candidate_name] += 1

# Print election results
print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {total_votes_count}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidate_votes_count.items():
    percentage = (votes / total_votes_count) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    # Determine the winner by looping iteratively over the key-value pairs in the candidate_votes_count dictionary
    if votes > winner_votes_count:
        election_winner = candidate
        winner_votes_count = votes

print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

# Write the election analysis to a text file
with open("analysis/election_results.txt", "w") as analysis_file:
    analysis_file.write("Election Results\n")
    analysis_file.write("-------------------------\n")
    analysis_file.write(f"Total Votes: {total_votes_count}\n")
    analysis_file.write("-------------------------\n")

    # Calculate and write the percentage of votes each candidate won
    for candidate, votes in candidate_votes_count.items():
        percentage = (votes / total_votes_count) * 100
        analysis_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    analysis_file.write("-------------------------\n")
    analysis_file.write(f"Winner: {election_winner}\n")
    analysis_file.write("-------------------------\n")
