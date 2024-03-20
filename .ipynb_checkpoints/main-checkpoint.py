import csv

# Path to the budget data CSV file
budget_data_csv = "PyBank/Resources/budget_data.csv"
# Path to the election data CSV file
election_data_csv = "PyPoll/Resources/election_data.csv"

# Initialize variables for PyBank analysis
months_count = 0
total_profit_loss = 0
previous_profit_loss = 0
total_profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", float('inf')]  # Initialize with positive infinity

# Read the CSV file for PyBank analysis
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)

    # Loop through each row in the CSV file for PyBank analysis
    for row in csvreader:
        # Increment total months
        months_count += 1

        # Calculate net total profit/loss
        total_profit_loss += int(row[1])

        # Calculate change in profit/loss
        if months_count > 1:
            change = int(row[1]) - previous_profit_loss
            total_profit_loss_change += change

            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        # Store current profit/loss for next iteration
        previous_profit_loss = int(row[1])

# Calculate average change for PyBank analysis
average_change = total_profit_loss_change / (months_count - 1)

# Print financial analysis for PyBank
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months_count}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the financial analysis to a text file for PyBank
with open("PyBank/analysis/financial_analysis.txt", "w") as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("----------------------------\n")
    analysis_file.write(f"Total Months: {months_count}\n")
    analysis_file.write(f"Total: ${total_profit_loss}\n")
    analysis_file.write(f"Average Change: ${average_change:.2f}\n")
    analysis_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Initialize variables for election analysis
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
    # Determine the winner
    if votes > winner_votes_count:
        election_winner = candidate
        winner_votes_count = votes

print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

# Write the election analysis to a text file
with open("PyPoll/analysis/election_results.txt", "w") as analysis_file:
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
