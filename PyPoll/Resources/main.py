#import os and csv
import os

import csv

#create path to election data csv
pypoll_csvpath = os.path.join("..", "Resources", "election_data.csv")

#set variables

#total votes
total_votes = [] 

#complete list of candidates who received votes
khan_can = 0
correy_can = 0
li_can = 0
otooley_can = 0

#reading through election data as csvreader
with open(pypoll_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None) # skip header row

    #read through each row of data
    for row in csvreader:

        #total number of votes
        total_votes.append(row[0])


        #winner of election based on popular vote


        #total number votes each candidate won
        if row[2] == "Khan":
            khan_can = khan_can + 1
        elif row[2] == "Correy":
            correy_can = correy_can + 1
        elif row[2] == "Li":
            li_can = li_can + 1
        elif row[2] == "O'Tooley": 
            otooley_can = otooley_can + 1


#winner of election based on popular vote
#create dictionary of candidates and total votes per candidate
#zip the two together to make a key that finds the max aka winner
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_can, correy_can, li_can, otooley_can]
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#change list to integer to use in the percent votes calculation
total_votes = int(len(total_votes))

#percent votes each candidate won with formatting to single decimal point
percent_khan = (khan_can / total_votes) * 100
formatted_khan = str(("{:.4}".format(percent_khan)))

percent_correy = (correy_can / total_votes) * 100
formatted_correy = str(("{:.4}".format(percent_correy)))

percent_li = (li_can / total_votes) * 100
formatted_li = str(("{:.4}".format(percent_li)))

percent_otooley = (otooley_can / total_votes) * 100
formatted_otooley = str(("{:.4}".format(percent_otooley)))

#print statements
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
print("Khan: " + formatted_khan + "% " + "(" + str(khan_can) + ")")
print("Correy: " + formatted_correy + "% " + "(" + str(correy_can) + ")")
print("Li: " + formatted_li + "% " + "(" + str(li_can) + ")")
print("O'Tooley: " + formatted_otooley + "% " + "(" + str(otooley_can) + ")")
print("----------------------------")
print("Winner: " + key)
print("----------------------------")

#export to text file
poll_output_txt_file = open("../analysis/Poll_Analysis.txt", "w")
poll_output_txt_file.write("Election Results")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("----------------------------")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("Total Votes: " + str(total_votes))
poll_output_txt_file.write("\n")
poll_output_txt_file.write("----------------------------")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("Khan: " + formatted_khan + "% " + "(" + str(khan_can) + ")")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("Correy: " + formatted_correy + "% " + "(" + str(correy_can) + ")")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("Li: " + formatted_li + "% " + "(" + str(li_can) + ")")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("O'Tooley: " + formatted_otooley + "% " + "(" + str(otooley_can) + ")")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("----------------------------")
poll_output_txt_file.write("\n")
poll_output_txt_file.write("Winner: " + key)
poll_output_txt_file.write("\n")
poll_output_txt_file.write("----------------------------")