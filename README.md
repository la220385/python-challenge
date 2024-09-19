"""
# Overview of Challenge 
The purpose of the Python script is to analyze the election data from a small town using a dataset (`election_data.csv`). The dataset contains the following information:
- Voter ID.
- County.
- Candidate.

# VS Code and Python were used to perform the following analysis:
1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate received.
5. The winner of the election based on popular vote.

# Steps Taken
1. I used Python's `csv` module to handle file operations and read the election data.
2. I then defined the path to the `election_data.csv` file to ensure the script knows where to look for the data.
3. I listed variables to track the total number of votes, candidate vote counts, and the winner of the election.
4. I used `csv.reader` to open and read each row of the CSV file.
5. For each row, I incremented the total number of votes and counted each candidate's vote.
6. I calculated the percentage of votes each candidate won based on their total vote count.
7. Then, I determined the candidate with the most votes to declare the election winner.
8. Outputted the results to the console in a well-formatted way.
9. Exported Results to a Text File: I saved the results to `election_results.txt` on my desktop and then to the analysis folder.

# These are the external sources used to analyze the data 
- I referred to the Python documentation on [reading and writing CSV files](https://docs.python.org/3/library/csv.html) to handle the CSV file in the challenge.
- Several portions of the script were influenced by discussions and solutions found on Stack Overflow (https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python)
- I also used information from [Real Python's article on reading and writing files](https://realpython.com/read-write-files-python/) to understand how to output the results to a text file.
- **Xpert Learning Assistant via BootCamp Spot**: Additional guidance and learning support were provided by Xpert Learning Assistant via BootCamp Spot.

# Other information
- No collaboration with peers was involved in this project.
- All referenced external code was appropriately adapted and cited.

