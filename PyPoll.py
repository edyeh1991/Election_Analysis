# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#import dependent functions
import csv
import os

#Assign variable to path of file to load
load_file = os.path.join('Resources', 'election_results.csv')

#Assign variable to save to file path
save_to_file = os.path.join('analysis','election_analysis.txt')

#Initialize total vote counter
total_votes = 0

#Start empy list of candidates
candidate_list = []

#Start empty dictionary of votes
candidate_votes = {}

#track winning candidate and winning count
winning_candidate = ""
winning_count = 0
winning_percent =  0

#Opens, read, assigns data to election_data
with open(load_file) as election_data:
    read_file = csv.reader(election_data)
    
    #Read headers
    headers = next(read_file)
    
    #Print each row in CSV file
    for row in read_file:
        #add total vote count
        total_votes += 1

        #print candidate name for each row
        candidate_name = row[2]
        
        #append name to candidate list if not already in list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

            #track candidate's votes count
            candidate_votes[candidate_name] = 0
        
        #Add vote to candidate's count
        candidate_votes[candidate_name] += 1

        

#Determine percent of votes for each candidate by looping through counts
#Iterate through candidate list
for candidates in candidate_votes:
    
    #retrieve vote count of a candidate
    votes = candidate_votes[candidates]

    #calculate percent of votes
    vote_percent = float(votes) / float(total_votes) * 100

    #print candidate name, count and percent
    print(f'{candidates}: {vote_percent:.1f}% ({votes:,})\n')
    
    #determine if votes greater than winning count
    if (votes > winning_count) and (vote_percent > winning_percent):
            
        #set winning_count = votes and winning_percent = vote_percent
        winning_count = votes
        winning_percent = vote_percent

        #set winning_candidate to candidate's name
        winning_candidate = candidates

winning_candidate_summary = (
    f'-----------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning percent: {winning_percent:.1f}%\n'
    f'------------------\n')

print(winning_candidate_summary)

#Print total vote count
print (total_votes)
print (candidate_list)
print (candidate_votes)

#Open save_to_file as write able txt file
# with open(save_to_file,'w') as txt_file:
#     #Write data to file
#     txt_file.write('Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson')





