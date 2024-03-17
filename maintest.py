import pandas as pd

# Path to the budget data CSV file
budget_data_csv = "PyBank/Resources/budget_data.csv"
# Path to the election data CSV file
election_data_csv = "PyPoll/Resources/election_data.csv"

# Read the CSV file for PyBank analysis using pandas
budget_data = pd.read_csv(budget_data_csv)

# Initialize variables for PyBank analysis
months_count = len(budget_data)
total_profit_loss = budget_data['Profit/Losses'].sum()
budget_data['Change'] = budget_data['Profit/Losses'].diff()
average_change = budget_data['Change'].mean()
greatest_increase = budget_data.loc[budget_data['Change'].idxmax(), ['Date', 'Change']]
greatest_decrease = budget_data.loc[budget_data['Change'].idxmin(), ['Date', 'Change']]

# Print financial analysis for PyBank
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months_count}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']:,.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']:,.0f})")

# Write the financial analysis to a text file for PyBank
with open("PyBank/analysis/financial_analysis.txt", "w") as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("----------------------------\n")
    analysis_file.write(f"Total Months: {months_count}\n")
    analysis_file.write(f"Total: ${total_profit_loss}\n")
    analysis_file.write(f"Average Change: ${average_change:.2f}\n")
    analysis_file.write(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']:,.0f})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']:,.0f})\n")

# Read the CSV file for election analysis using pandas
election_data = pd.read_csv(election_data_csv)

# Initialize variables for election analysis
total_votes_count = len(election_data)
candidate_votes_count = election_data['Candidate'].value_counts()
election_winner = candidate_votes_count.idxmax()
winner_votes_count = candidate_votes_count.max()

# Print election results
print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {total_votes_count}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidate_votes_count.items():
    percentage = (votes / total_votes_count) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

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

