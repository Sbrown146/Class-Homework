import os
import csv

#List Declarations
Voter_ID = []
County = []
Candidate = []
UniqueCandidate = []
Winner = []

#Function to find the index for the max value of a list
def Max_Index(x):
    max_val = max(x)
    max_idx = x.index(max_val)
    return max_idx

#Function to tally up a candidates percentage total using their index within the
#UniqueCandidate List
def CandidateTotal(y):
    CandIndex = UniqueCandidate[y]
    CandCount = ((Candidate.count(CandIndex))/Total)*100
    return CandCount
    
#Procedure to read in csv file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader) #Skip header
    for row in csvreader:
        Voter_ID.append(row[0]) #List for Voter ID numbers
        County.append(row[1]) #List for Counties
        Candidate.append(row[2]) #List with Candidate names

        #The goal here is to get a list with just the 4 candidate names: Khan, Correy, Li and O'Tooley.  
        #This is done in three steps: First, set the Candidate list in the new list UniqueCandidate.
        #The set function will return the unique values but in a random order with each run so it must then
        #be sorted using the Candidate index.  Finally, it is then put back as a list for further evaluation.

UniqueCandidate = set(Candidate)
UniqueCandidate = sorted(set(Candidate), key=Candidate.index)
UniqueCandidate = list(UniqueCandidate)

#The len function will yield the total votes cast.
Total = len(Voter_ID)

#These 4 variables utilize the CandidateTotal macro to find the percentage total for each candidate based
#on their position in the UniqueCandidate list.  For example, UniqueCandidate[0] = Khan.
CandTotal1 = CandidateTotal(0)
CandTotal2 = CandidateTotal(1)
CandTotal3 = CandidateTotal(2)
CandTotal4 = CandidateTotal(3)

#Each candidates percentage total is put into a list where the Max_Index function is run to find the index
#of the largest value for the winner.
Winner = [CandTotal1, CandTotal2, CandTotal3, CandTotal4]
WinnerIndex = Max_Index(Winner)

#This outputs what is displayed in the terminal into a csv file.  File = datafile is added to the end of each print
#statement for proper outputing to the csv file.
with open('PythonHW_Part2_Election_Results_SDB.csv', 'w') as datafile:
    print("", file = datafile)
    print("Election Results")
    print("--------------------------------", file = datafile)
    print(f"Total Votes: {Total}", file = datafile)
    print("--------------------------------", file = datafile)
    #Each of these 4 rows output the candidates name using the UniqueCandidate list, their percentage total with the
    #CandidateTotal function (rounded to 3 decimal places), and uses Candidate.count(UniqueCandidate[]) to display the
    #total amount of votes won by counting how many times the candidates name appears in the original Candidate list.
    print(f"{UniqueCandidate[0]}: {round(CandTotal1, 3)}% ({Candidate.count(UniqueCandidate[0])})", file = datafile)
    print(f"{UniqueCandidate[1]}: {round(CandTotal2, 3)}% ({Candidate.count(UniqueCandidate[1])})", file = datafile)
    print(f"{UniqueCandidate[2]}: {round(CandTotal3, 3)}% ({Candidate.count(UniqueCandidate[2])})", file = datafile)
    print(f"{UniqueCandidate[3]}: {round(CandTotal4, 3)}% ({Candidate.count(UniqueCandidate[3])})", file = datafile)
    print("--------------------------------", file = datafile)
    #The winner is determined using the WinnerIndex number within the UniqueCandidate list.
    print(f"And The Winner is: {UniqueCandidate[WinnerIndex]}!", file = datafile)
    print(f"   Congratulations {UniqueCandidate[WinnerIndex]}!", file = datafile)
    print("--------------------------------", file = datafile)
    print("", file = datafile)


#Terminal Output
print("")
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {Total}")
print("--------------------------------")
#Each of these 4 rows output the candidates name using the UniqueCandidate list, their percentage total with the
#CandidateTotal function (rounded to 3 decimal places), and uses Candidate.count(UniqueCandidate[]) to display the
#total amount of votes won by counting how many times the candidates name appears in the original Candidate list.
print(f"{UniqueCandidate[0]}: {round(CandTotal1, 3)}% ({Candidate.count(UniqueCandidate[0])})")
print(f"{UniqueCandidate[1]}: {round(CandTotal2, 3)}% ({Candidate.count(UniqueCandidate[1])})")
print(f"{UniqueCandidate[2]}: {round(CandTotal3, 3)}% ({Candidate.count(UniqueCandidate[2])})")
print(f"{UniqueCandidate[3]}: {round(CandTotal4, 3)}% ({Candidate.count(UniqueCandidate[3])})")
print("--------------------------------")
#The winner is determined using the WinnerIndex number within the UniqueCandidate list.
print(f"And The Winner is: {UniqueCandidate[WinnerIndex]}!")
print(f"   Congratulations {UniqueCandidate[WinnerIndex]}!")
print("--------------------------------")
print("")