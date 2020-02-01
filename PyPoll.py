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

#Opens, read, assigns data to election_data
with open(load_file) as election_data:
    read_file = csv.reader(election_data)
    
    #Print headers
    headers = next(read_file)
    print(headers)
    
    #Print each row in CSV file
    # for row in read_file:
    #     print (row)

#Open save_to_file as write able txt file
with open(save_to_file,'w') as txt_file:
    #Write data to file
    txt_file.write('Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson')





