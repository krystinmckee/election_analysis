# Data we want to retrieve:
    # 1. Total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. Total number of votes each candidate received
    # 4. Percentage of votes each candidate won
    # 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

# TO DO: Read and analyze the data here
   
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)  
    

    # Print the header row.
    headers = next(file_reader)
    print(headers)



# Using the with function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


