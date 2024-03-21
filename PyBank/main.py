import csv

# Path to the budget data CSV file
budget_data_csv = "Resources/budget_data.csv"

# Initialize variables for PyBank analysis
months_count = 0
total_profit_loss = 0
previous_profit_loss = 0
total_profit_loss_change = 0
greatest_increase = ["", 0] # ensures that any increase encountered during the iteration will be larger than this initial value
greatest_decrease = ["", float('inf')]  # Initialize with positive infinity to ensure iteration will be smaller than the initial value

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

        # Calculate change in profit/loss between the current month and the previous month
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
with open("analysis/financial_analysis.txt", "w") as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("----------------------------\n")
    analysis_file.write(f"Total Months: {months_count}\n")
    analysis_file.write(f"Total: ${total_profit_loss}\n")
    analysis_file.write(f"Average Change: ${average_change:.2f}\n")
    analysis_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

