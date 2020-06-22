# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create list of Counties
My_list=["Arapahoe","Denver","Jefferson"]
print(My_list)

# Dictonary County is Key and vote casted by county is value
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
county_options = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_county = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_results:
    file_reader = csv.reader(election_results)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if county_name not in county_options:
            # Add the candidate name to the candidate list.
            county_options.append(county_name)
            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count.
        county_votes[county_name] += 1
print(county_votes)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    county_summary = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n")
    print(county_summary, end="")
   # Collect county results showing county, county count, county percentage
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(county_summary, end="")
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county
            winning_percentage = vote_percentage

# Print the winning candidate's results to the terminal.
    county_summary = (
        f"-------------------------\n"
        f"Largest Voter Turnout: {winning_county}\n")
    print(county_summary, end="") 

    #Determine loser vote count, loser percentage, and loser candidate.
    if (votes < winning_count) and (vote_percentage < winning_percentage):
            loser_count = votes
            loser_county = county
            loser_percentage = vote_percentage
    # Print the loser candidate's results to the terminal.
    ounty_summary = (
        f"lowest Voter Turnout: {loser_county}\n")
    print(county_summary, end="")
    # Save the final vote count to the text file.
    txt_file.write(county_summary)

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "a") as txt_file:
    # Print the final vote count to the terminal.
    candidate_summary = (
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(candidate_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
     
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    candidate_summary = (
        f"-------------------------\n"
        f"Winner Candidate:\n\n"
        f"Winning Candidate: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")
    print(candidate_summary)

    # Determine loser vote count, loser percentage, and loser candidate.
    if (votes < winning_count) and (vote_percentage < winning_percentage):
            loser_count = votes
            loser_candidate = candidate
            loser_percentage = vote_percentage
    # Print the loser candidate's results to the terminal.
    candidate_summary = (
        f"Loser Candidate:\n\n"
        f"Losing Candidate: {loser_candidate}\n"
        f"Vote Count: {loser_count:,}\n"
        f"Percentage: {loser_percentage:.1f}%\n"
        f"-------------------------\n")
    print(candidate_summary)

    #  Save the candidate results to our text file.
    txt_file.write(candidate_summary)
