#Determine election results by candidate and county
#Display total votes in election, total votes and percent per county and per candidate 
#Display Largest county turnout and election winner

#import dependent functions
import csv
import os

#Assign variable to path of file to load
load_file = os.path.join('Resources', 'election_results.csv')

#Assign variable to save to file path
save_to_file = os.path.join('analysis','election_analysis.txt')

#Initialize total vote counter and 
total_votes = 0

#Start empty list of candidates
candidate_list = []

#Start empty dictionary of votes per candidate
candidate_votes = {}

#start empty list of counties
counties_list =[]

#start empty dictionary of votes per county
county_votes = {}

#Opens, read, assigns data to election_data
with open(load_file) as election_data:
    read_file = csv.reader(election_data)
    
    #read headers
    headers = next(read_file)
    
    #tabulate total vote count
    for row in read_file:
        total_votes += 1

        #determine county and candidate name for each row
        county = row[1]
        candidate_name = row[2]

        #append county to county list if not already in list
        if county not in counties_list:
            counties_list.append(county)

        #track county's vote count
            county_votes[county] = 0

        #tabulate county votes
        county_votes[county] += 1

        #append name to candidate list if not already in list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

        #track candidate's votes count
            candidate_votes[candidate_name] = 0
        
        #tabulate candidate votes
        candidate_votes[candidate_name] += 1

#Save results to txt file        
with open(save_to_file,'w') as txt_file:

    #print final vote count
    election_results = (
        f'\nElection Results\n'
        f'---------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'----------------------\n\n')
    print (election_results, end = "")

    #save file to txt file
    txt_file.write(election_results)

    print ('County Votes:\n')

    #write County Votes header
    county_votes_header = ('County Votes:\n')
    txt_file.write(county_votes_header)

    #track winning county and winning count
    winning_county = ""
    winning_count = 0
    winning_percent =  0

    #determine percent of votes for each county by looping through counts
    for county in county_votes:
        #retrieve vote count of county
        votes = county_votes[county]

        #calculate percent of vote by county
        vote_percent = float(votes) / float(total_votes) *100

        #print county name, count and percent
        county_results = (f'{county}: {vote_percent:.1f}% ({votes:,})\n')
        print(county_results)
    
        #save results to txt file
        txt_file.write(county_results)
    
    #determine Largest County Turnout
        if (votes > winning_count) and (vote_percent > winning_percent):
                
            #set winning_count = votes and winning_percent = vote_percent
            winning_count = votes
            winning_percent = vote_percent

            #set winning_county to candidate's name
            winning_county = county

    #print winning county summary
    winning_county_summary = (
        f'\n---------------------------\n'
        f'Largest County Turnout: {winning_county}\n'
        f'---------------------------\n')
    print(winning_county_summary)

    #save results to txt file
    txt_file.write(winning_county_summary)

    #determine percent of votes for each candidate by looping through counts
    #iterate through candidate list
    
    #track winning candidate and winning count
    winning_candidate = ""
    winning_count = 0
    winning_percent =  0
    
    for candidates in candidate_votes:
        
        #retrieve vote count of a candidate
        votes = candidate_votes[candidates]

        #calculate percent of votes
        vote_percent = float(votes) / float(total_votes) * 100

        #print candidate name, count and percent
        candidate_results = (f'{candidates}: {vote_percent:.1f}% ({votes:,})\n')
        print (candidate_results)

        #save results to txt file
        txt_file.write(candidate_results)


        #determine if votes greater than winning count
        if (votes > winning_count) and (vote_percent > winning_percent):
                
            #set winning_count = votes and winning_percent = vote_percent
            winning_count = votes
            winning_percent = vote_percent

            #set winning_candidate to candidate's name
            winning_candidate = candidates

    #print winning candidate summary
    winning_candidate_summary = (
        f'---------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning percent: {winning_percent:.1f}%\n'
        f'---------------------------\n')

    print(winning_candidate_summary)

    #save winning candidate to txt file
    txt_file.write(winning_candidate_summary)