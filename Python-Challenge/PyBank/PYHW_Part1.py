import os
import csv

#List Declarations
Everything = []
Dates = []
PL = []
MaxPL = []
MinPL = []
MuPL = []

#Numeric Variable Declarations
MaxIndex = 0
MinIndex = 0

#Macro Declarations
#This macro gets the average by dividing its sum by its length
def Average(x):
    return sum(x)/len(x)

#Macro to find the index for the max value of a list
def Max_Index(x):
    max_val = max(x)
    max_idx = x.index(max_val)
    return max_idx #max_val

#Macro to find the index for the minimum value of a list
def Min_Index(y):
    min_val = min(y)
    min_idx = y.index(min_val)
    return min_idx #min_val

#Procedure to read in csv file.
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    header=next(csv_reader) #Skips header
    for stuff in csv_reader:
        Dates.append(stuff[0]) #List for Dates
        PL.append(stuff[1]) #List for Profit/Losses
        #Unfortunately, since PL is created as a list, the data is not in a proper numeric form which 
        #will cause issues with numeric calculation.  This line will set every element in the PL list
        #as a float variable to correct this problem.
        PL = [float(i) for i in PL]
        MaxPL = sorted(PL, reverse=True) #Sorts PL list in reverse for descending order
        MinPL = sorted(PL) #Sorts PL list in ascending order
        MuPL = Average(PL) #Gets the average for the PL list
        MaxIndex = Max_Index(PL) #Uses Max_Index Macro to find index of Max value in PL list
        MinIndex = Min_Index(PL) #Uses Max_Index Macro to find index of Minimum value in PL list

#with open(os.path.join("Budget_Results_SDB", "w", newline="") as datafile:
#with open('Budget_Results_SDB.csv', 'w') as datafile
   # writer=csv.writer(datafile)

#This outputs what is displayed in the terminal into a csv file.  File = datafile is added to the end of each print
#statement for proper outputing to the csv file.
with open('PythonHW_Part1_Budget_Results_SDB.csv', 'w') as datafile:
    print("", file=datafile)
    print("Financial Analysis", file = datafile)
    print("--------------------------", file = datafile)
    print(f"Total Months: {len(Dates)}", file = datafile) #len(Dates) displays the total Months.
    print(f"Total: ${int(sum(PL))}", file = datafile) #int(sum(PL)) display the total of the PL list as an integer.
    print(f"Average Change: ${round(MuPL, 2)}", file = datafile) #display the average change, rounded to 2 decimal places.
    #These 2 lines display the min/max profits using the respective MaxIndex or MinIndex numbers for positioning within
    #the Dates and PL list.  The PL list is put into an integer form to display without an decimal places.
    print(f"Greatest Increase in Profits: {Dates[MaxIndex]} (${int(PL[MaxIndex])})", file = datafile)
    print(f"Greatest Decrease in Profits: {Dates[MinIndex]} (${int(PL[MinIndex])})", file = datafile)

#Terminal Output
print("")
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(Dates)}") #len(Dates) displays the total Months.
print(f"Total: ${int(sum(PL))}") #int(sum(PL)) display the total of the PL list as an integer.
print(f"Average Change: ${round(MuPL, 2)}") #display the average change, rounded to 2 decimal places.
#These 2 lines display the min/max profits using the respective MaxIndex or MinIndex numbers for positioning within
#the Dates and PL list.  The PL list is put into an integer form to display without an decimal places.
print(f"Greatest Increase in Profits: {Dates[MaxIndex]} (${int(PL[MaxIndex])})")
print(f"Greatest Decrease in Profits: {Dates[MinIndex]} (${int(PL[MinIndex])})")
