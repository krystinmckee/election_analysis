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

#Initialize total vote counter to 0
total_votes = 0
#Declare list for candidate names
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:



# TO DO: Read and analyze the data here
   
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)  
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        
        #Print the candidate name from each row
        candidate_name = row[2]
        
        # Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
           
         # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# 1. Total number of votes cast
###print(total_votes)

# 2. A complete list of candidates who received votes
###print(candidate_options)

# 3. Total number of votes each candidate received
###print(candidate_votes)

#4. Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes.
    ###print(f"{candidate_name}: received {vote_percentage}% of the vote")

# 5. The winner of the election based on popular vote
    #  To do: print out the winning candidate, vote count and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




# Using the with function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


