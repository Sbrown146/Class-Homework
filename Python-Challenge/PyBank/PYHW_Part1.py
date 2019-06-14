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

with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    header=next(csv_reader)
    for stuff in csv_reader:
        Dates.append(stuff[0])
        PL.append(stuff[1])
        PL = [float(i) for i in PL]
        MaxPL = sorted(PL, reverse=True)
        MinPL = sorted(PL)
        MuPL = Average(PL)
        MaxIndex = Max_Index(PL)
        MinIndex = Min_Index(PL)

#with open(os.path.join("Budget_Results_SDB", "w", newline="") as datafile:
#with open('Budget_Results_SDB.csv', 'w') as datafile
   # writer=csv.writer(datafile)

with open('PythonHW_Part1_Budget_Results_SDB.csv', 'w') as datafile:
    print("", file=datafile)
    print("Financial Analysis", file = datafile)
    print("--------------------------", file = datafile)
    print(f"Total Months: {len(Dates)}", file = datafile)
    print(f"Total: ${int(sum(PL))}", file = datafile)
    print(f"Average Change: ${round(MuPL, 2)}", file = datafile)
    print(f"Greatest Increase in Profits: {Dates[MaxIndex]} (${int(PL[MaxIndex])})", file = datafile)
    print(f"Greatest Decrease in Profits: {Dates[MinIndex]} (${int(PL[MinIndex])})", file = datafile)

print("")
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(Dates)}")
print(f"Total: ${int(sum(PL))}")
print(f"Average Change: ${round(MuPL, 2)}")
print(f"Greatest Increase in Profits: {Dates[MaxIndex]} (${int(PL[MaxIndex])})")
print(f"Greatest Decrease in Profits: {Dates[MinIndex]} (${int(PL[MinIndex])})")
