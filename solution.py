import json

filename = input("Enter file name: ")

jsonfile = open(filename) 

data = json.load(jsonfile)

expenseData = data["expenseData"]
revenueData = data["revenueData"]

mergedRevenueData = {}
mergedExpenseData = {}

for revenue in revenueData:
    if revenue["startDate"] not in mergedRevenueData:
        mergedRevenueData[revenue["startDate"]] = revenue["amount"]
    else :
        mergedRevenueData[revenue["startDate"]]  = mergedRevenueData[revenue["startDate"]] + revenue["amount"]

    if revenue["startDate"] not in mergedExpenseData:
        mergedExpenseData[revenue["startDate"]] = 0

for expense in expenseData:
    if expense["startDate"] not in mergedExpenseData:
        mergedExpenseData[expense["startDate"]] = expense["amount"]
    else :
        mergedExpenseData[expense["startDate"]] =  mergedExpenseData[expense["startDate"]] + expense["amount"]

    if expense["startDate"] not in mergedRevenueData:
        mergedRevenueData[expense["startDate"]] = 0

myKeys = list(mergedRevenueData.keys())
myKeys.sort()
sortedRevenueData = {i: mergedRevenueData[i] for i in myKeys}
sortedExpenseData = {i: mergedExpenseData[i] for i in myKeys}

balanceList = []

revenueValues = list(sortedRevenueData.values())
expenseValues = list(sortedExpenseData.values())

dateValues = list(sortedExpenseData.keys())

minDate = dateValues[0]
maxDate = dateValues[-1]
newKeys = []
currDate = minDate

while(currDate != maxDate) :
    newKeys.append(currDate)

    month = int(currDate[5:7])
    month = month + 1
    year = int(currDate[0:4])
    if month > 12:
        year =  int(currDate[0:4])
        year = year + 1 
        month = 1
    
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    year = str(year)
    
    newDate = year + "-" + month + currDate[7:]
    currDate = newDate

newKeys.append(currDate)


i = 0
for key in newKeys:
    if key not in dateValues:
         balanceList.append({"amount" : 0, "startDate" : key})
    else:
        balanceAmount = revenueValues[i] - expenseValues[i]
        balanceList.append({"amount" : balanceAmount, "startDate" : key})
        i = i+1


outputDict = {"balance" : balanceList}
outputJson = json.dumps(outputDict, indent = 2) 
print(outputJson)
