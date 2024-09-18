import csv

file_path = '/Users/latifahjones/Desktop/python-challenge/Pypoll/Resources/election_data.csv'

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(file_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100

    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("election_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100

file.write("-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-------------------------\n") 