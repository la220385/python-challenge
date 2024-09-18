# Overview of Challenge 
The purpose of the Python script is to analyze the financial records of a company using a dataset (`budget_data.csv`). The dataset contains the following information:
- Date(month and year).
- Profit/Losses

# VS code and Python was used to perform the following analysis:
1. Total number of months included in the dataset.
2. Net total amount of "Profit/Losses" over the entire period.
3. Average change in "Profit/Losses" between months.
4. Greatest increase in profits (date and amount).
5. Greatest decrease in profits (date and amount).

# Steps Taken
1. I used Python's `csv` and `os` modules to handle file operations and manage file paths.
2. I then defined the path to the `budget_data.csv` file to ensure the script knows where to look for the data.
3. Listed variables to track totals, monthly changes, and the greatest increases/decreases in profit.
4. Used `csv.reader` to open and read each row of the CSV file.
5. For each row, incremented the total number of months and summed up the profits/losses.
6. I calculated the change in profit between months, starting from the second month.
7. Then computed the average of the monthly changes.
8. Outputted the results to the console in a well-formatted way.
9. Exported Results to a Text File: I saved the results to `financial_analysis.txt` on my desktop and then to the analysis folder. 

# These are the external sources used to analyze the data 
- I referred to the Python documentation on [reading and writing CSV files](https://docs.python.org/3/library/csv.html) to handle the CSV file in the challenge.
- Several portions of the script were influenced by discussions and solutions found on Stack Overflow (https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python)
- I also used information from [Real Python's article on reading and writing files](https://realpython.com/read-write-files-python/) to understand how to output the results to a text file.
 - Xpert Learning Assistant via BootCamp Spot: Additional guidance and learning support were provided by Xpert Learning Assistant via BootCamp Spot.

 # Other information
- No collaboration with peers was involved in this project.
- All referenced external code was appropriately adapted and cited.
