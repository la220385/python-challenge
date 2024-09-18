import csv
import os

file_path = '/Users/latifahjones/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

total_months = 0
net_total = 0
changes = []
previous_profit = None
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        total_months += 1

        net_total += profit

        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date

            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        previous_profit = profit

if len(changes) > 0:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)  

print(output)

output_file_path = '/Users/latifahjones/Desktop/financial_analysis.txt'

with open(output_file_path, 'w') as text_file:
    text_file.write(output)

print(f"Financial analysis exported to {output_file_path}")