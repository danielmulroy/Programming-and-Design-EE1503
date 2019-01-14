f=open("results.txt") #open the file
import math #for use with statistics later
import statistics
import json

##taking all of the data and putting it into nested lists. 50 in each nest for each piece of data
dan_data = []
for line in f:
    dan_data.append([float(x) for x in line.split()])

#generates 4 lists for each row of data, and another of the sorted data for ease later. Also another sorted nest for binary search
TestNo = dan_data[0]
TestNo = list(map(int, TestNo)) #removes the decimal point
TestDate = dan_data[1]
TestTime = dan_data[2]
Result = dan_data[3]
SortedResult = Result[:]
SortedResult.sort()
revSortedResult = SortedResult[::-1]
sdan_dataen = TestNo[:]
sdan_datadate = dan_data[1][:]
sdan_datatime = dan_data[2][:]
sdan_dataresult = dan_data[3][:]
sdan_data = [sdan_dataen,sdan_datadate,sdan_datatime,sdan_dataresult]

for i in range(0,len(sdan_data[3])-1):
    for j in range(i+1,len(sdan_data[3])):
        if sdan_data[3][i]>sdan_data[3][j]:
            sdan_data[0][i], sdan_data[0][j] = sdan_data[0][j], sdan_data[0][i]
            sdan_data[1][i], sdan_data[1][j] = sdan_data[1][j], sdan_data[1][i]
            sdan_data[2][i], sdan_data[2][j] = sdan_data[2][j], sdan_data[2][i]
            sdan_data[3][i], sdan_data[3][j] = sdan_data[3][j], sdan_data[3][i]

"""
THESE ARE THE FUNCTIONS
"""
def FindMeanAve(x):
    average = 0
    for i in x:
        average=average+i
    average = average/(len(x))
    while True:
        try:
            rnd = int(input("How many decimal places do you want the mean average rounding to? "))
            if rnd < 0:
                print("Sorry, input must be a positive integer, please try again")
                continue
            break
        except ValueError:
            print("Not a valid input! Please try again. ")
    if rnd==1:
        print("The mean average value to",rnd,"decimal place is",round(average, rnd))
    else:
        print("The mean average value to",rnd,"decimal places is",round(average, rnd))

def FindMediAve(x):
    while True:
        try:
            rnd = int(input("How many decimal places do you want the median average rounding to? "))
            if rnd < 0:
                print("Sorry, input must be a positive integer, please try again")
                continue
            break
        except ValueError:
            print("Not a valid input! Please try again. ")
    if rnd==1:
        print("The median average value to",rnd,"decimal place is",round(statistics.median(x), rnd))
    else:
        print("The median average value to",rnd,"decimal places is",round(statistics.median(x), rnd))

def StandardDeviation(x): 
    var = 0
    average = 0
    for i in x:
        average=average+i
    average = average/(len(x))
    
    for i in x:
        var = var + (i - average)**2
    var = var/(len(x))
    while True:
        try:
            rnd = int(input("How many decimal places do you want the standard deviation rounding to? "))
            if rnd < 0:
                print("Sorry, input must be a positive integer, please try again")
                continue
            break
        except ValueError:
            print("Not a valid input! Please try again. ")
    if rnd==1:
        print("The standard deviation to",rnd,"decimal place is",round(math.sqrt(var), rnd))
    else:
        print("The standard deviation to",rnd,"decimal places is",round(math.sqrt(var), rnd))

def Higher(x):
    while True:
        try:
            high=float(input("Please enter the value from which you'd like to search: "))
            break
        except ValueError:
            print("Not a valid input! Please try again. ")
    print("There are",len([1 for i in x if i > high]),"values greater than",high)

def Sort(z):
    while True:
        x=input("Would you like the list in acsending(a) or decending(d) order? Please enter a or d: ")
        if not ((x=="a") or (x=="d")):
            print("Not an a or d! Please try again. ")
        else:
            break
    while True:
        y=input("Would you like the ordered list of results displayed? Please enter yes or no: ")
        if not ((y=="yes") or (y=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if x=="a" and y=="yes":
        print(z)
    elif x=="d" and y=="yes":
        print(z[::-1])

def EditResult(x):##x=location in sorted list
    m = sdan_data[3][x]
    while True:
        try:
            dan_data[3][dan_data[3].index(m)]=float(input("Please enter the value you'd like to change this result to: "))
            break
        except ValueError:
            print("Not a valid input! Please try again. ")    
    sdan_data[3][x]=dan_data[3][dan_data[3].index(m)]
def AddResult():
    dan_data[0].append(float(dan_data[0][-1]+1))
    while True:
        try:
            dan_data[1].append(float(input("Please enter the date on which the data was recorded in the form dd.mm: ")))
            if dan_data[1][-1] < 0 or dan_data[1][-1] > 32:
                print("Not a valid input! Please try again. ")
                continue
            break
            break
        except ValueError:
            print("Not a valid input! Please try again. ")    
    while True:
        try:
            dan_data[2].append(float(input("Please enter the time at which the data was recorded in the form hh.mm: ")))
            if dan_data[2][-1] < 0 or dan_data[2][-1] > 24:
                print("Not a valid input! Please try again. ")
                continue
            break
        except ValueError:
            print("Not a valid input! Please try again. ")    
    while True:
        try:
            dan_data[3].append(float(input("Please enter the new result: ")))
            break
        except ValueError:
            print("Not a valid input! Please try again. ")    
    while True:
        wouldyoulikeadd = input("Would you like to add another new result to the data? Please enter yes or no: ")
        if not ((wouldyoulikeadd=="yes") or (wouldyoulikeadd=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikeadd=="yes":
        AddResult()
    else:
        SaveNewFile()

def SaveNewFile():
    name = input("What do you want to name the new file where the data is to be stored? ") + ".txt"

    fa=open(name,"a")
    outgoing = dan_data[:]
    o0 = str(outgoing[0]).strip("[]")
    o1 = str(outgoing[1]).strip("[]")
    o2 = str(outgoing[2]).strip("[]")
    o3 = str(outgoing[3]).strip("[]")
    o0 = o0.replace(",","")
    o1 = o1.replace(",","")
    o2 = o2.replace(",","")
    o3 = o3.replace(",","")
    fa.write(o0)
    fa.write("\n")
    fa.write(o1)
    fa.write("\n")
    fa.write(o2)
    fa.write("\n")
    fa.write(o3)
    fa.close()


def FullDataAnalysis():
    while True:
        wouldyoulikemaxmin = input("For the set of data, would you like the maximum and minimum results? Please enter yes or no: ")
        if not ((wouldyoulikemaxmin=="yes") or (wouldyoulikemaxmin=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikemaxmin=="yes":
        print("The largest measured value was",SortedResult[-1],"and the smallest was",SortedResult[0])
        
    while True:
        wouldyoulikeave = input("For the set of data, would you like to find the average value? Please enter yes or no: ") ##IF TIME ALLOWS, ADD OTHER AVERAGES, MODE, MEDIAN
        if not ((wouldyoulikeave=="yes") or (wouldyoulikeave=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikeave=="yes":
        while True:
            meanmedian=input("Would you like to find the mean average, median average, or both? Please enter mean, median or both. ")
            if not ((meanmedian=="mean") or (meanmedian=="median") or (meanmedian=="both")):
                print("Not a valid answer! Please try again. ")
            else:
                break
        if meanmedian=="mean":
            FindMeanAve(Result)
        if meanmedian=="median":
            FindMediAve(Result)
        if meanmedian=="both":
            FindMeanAve(Result)
            FindMediAve(Result)
        
    while True:
        wouldyoulikestadev = input("For the set of data, would you like the standard deviation? Please enter yes or no: ")
        if not ((wouldyoulikestadev=="yes") or (wouldyoulikestadev=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikestadev=="yes":
        StandardDeviation(Result)

    while True:
        wouldyoulikehigher = input("For the set of data, would you like to calculate how many results are greater than an input value? Please enter yes or no: ")
        if not ((wouldyoulikehigher=="yes") or (wouldyoulikehigher=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikehigher=="yes":
        Higher(Result)

    while True:
        wouldyoulikesort = input("For the set of data, would you like to sort the results? Please enter yes or no: ")
        if not ((wouldyoulikesort=="yes") or (wouldyoulikesort=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikesort=="yes":
        Sort(SortedResult)

def PartialDataAnalysis():
    while True:
        whichpart = input("Would you like to choose data by date, by time, or by experiment number(en)? Please enter date, time or en: ")
        if not ((whichpart=="date") or (whichpart=="time") or(whichpart=="en")):
            print("Not a valid response! Please try again. ")
        else:
            break

    if whichpart=="date":
        while True:
            try:
                z=float(input("For day would you like results? (In the form dd.mm) "))
                break
            except ValueError:
                print("Not a valid input! Please try again. ")
        chosen=[i for i,x in enumerate(TestDate) if x == z]

    elif whichpart=="time":
        while True:
            try:
                y=float(input("Between which times would you like to analyse? Enter the lower bound in the form hh.mm followed by the enter key "))
                break
            except ValueError:
                print("Not a valid input! Please try again. ")
        while True:
            try:
                z=float(input("Enter the upper bound in the form hh.mm: "))
                break
            except ValueError:
                print("Not a valid input! Please try again. ")
        chosen=[i for i,x in enumerate(TestTime) if y<=x<=z]

    elif whichpart=="en":
        while True:
            try:
                y=int(input("Between which experiment numbers would you like to analyse? Enter the lower bound value: "))
                break
            except ValueError:
                print("Not a valid input! Please try again. ")
        while True:
            try:
                z=int(input("Enter the upper bound value: "))
                break
            except ValueError:
                print("Not a valid input! Please try again. ")
        chosen=[i for i,x in enumerate(TestNo) if y<=x<=z]

    chosenresults = []    
    for x in chosen:
        chosenresults.append(Result[x])
    sortchosenresults = chosenresults[:]
    sortchosenresults.sort()
    
    while True:
        wouldyouliketoprint = input("Would you like to print all of the chosen data for reference? Please enter yes or no: ")
        if not ((wouldyouliketoprint=="yes") or (wouldyouliketoprint=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyouliketoprint=="yes":
        for x in chosen:
            print('{0:2n} {1:4g} {2:g} {3:g}'.format(TestNo[x], TestDate[x], TestTime[x], Result[x]))
        print("The data is in the form: Test Number, Date (dd.mm), Time, Result")

    while True:
        wouldyoulikemaxmin = input("For the selected set of data, would you like the maximum and minimum results? Please enter yes or no: ")
        if not ((wouldyoulikemaxmin=="yes") or (wouldyoulikemaxmin=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikemaxmin=="yes":
        print("The largest selected result was",sortchosenresults[-1],"and the smallest was",sortchosenresults[0])

    while True:
        wouldyoulikeave = input("For the selected set of data, would you like to find the average value? Please enter yes or no: ") 
        if not ((wouldyoulikeave=="yes") or (wouldyoulikeave=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikeave=="yes":
        while True:
            meanmedian=input("For the selected set of data, would you like to find the mean average, median average, or both? Please enter mean, median or both. ")
            if not ((meanmedian=="mean") or (meanmedian=="median") or (meanmedian=="both")):
                print("Not a valid answer! Please try again. ")
            else:
                break
        if meanmedian=="mean":
            FindMeanAve(chosenresults)
        if meanmedian=="median":
            FindMediAve(chosenresults)
        if meanmedian=="both":
            FindMeanAve(chosenresults)
            FindMediAve(chosenresults)

    while True:
        wouldyoulikestadev = input("For the selected set of data, would you like the standard deviation? Please enter yes or no: ")
        if not ((wouldyoulikestadev=="yes") or (wouldyoulikestadev=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikestadev=="yes":
        StandardDeviation(chosenresults)

    while True:
        wouldyoulikehigher = input("For the selected set of data, would you like to calculate how many results are greater than an input value? Please enter yes or no: ")
        if not ((wouldyoulikehigher=="yes") or (wouldyoulikehigher=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikehigher=="yes":
        Higher(chosenresults)

    while True:
        wouldyoulikesort = input("For the selected set of data, would you like to sort the results? Please enter yes or no: ")
        if not ((wouldyoulikesort=="yes") or (wouldyoulikesort=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikesort=="yes":
        Sort(sortchosenresults)

def BinarySearch():
    while True:
        try:
            value=float(input("Please enter the result for which you'd like to search: "))
            if value < 0:
                print("Sorry, there are no negative results, please try again")
                continue
            break
        except ValueError:
            print("Not a valid input! Please try again. ")
        break
    min=0
    max = len(sdan_data[3])-1
    
    while True:
        if max < min:
            print("The value",value,"has not been found, but the closest value",sdan_data[3][m],"has been found in experiment number",sdan_data[0][m],"which was performed on day",sdan_data[1][m],"at time",sdan_data[2][m])
            break
        
        m = ((min+max) // 2)
        
        if sdan_data[3][m] < value:
            min = m + 1
        elif sdan_data[3][m] > value:
            max = m - 1
        
        else:
            print("The value",sdan_data[3][m],"has been found in experiment number",sdan_data[0][m],"which was performed on day",sdan_data[1][m],"at time",sdan_data[2][m])
            break
    while True:
        wouldyoulikeedit = input("Would you like to edit this result? Please enter yes or no: ")
        if not ((wouldyoulikeedit=="yes") or (wouldyoulikeedit=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break            
    if wouldyoulikeedit=="yes":
        EditResult(m)    
    while True:
        wouldyoulikesearch = input("Would you like to search for or edit another specific piece of data by result? Please enter yes or no: ")
        if not ((wouldyoulikesearch=="yes") or (wouldyoulikesearch=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break            
    if wouldyoulikesearch=="yes":
        BinarySearch()
    while True:
        wouldyoulikeadd = input("Would you like to add a new result to the data? Please enter yes or no: ")
        if not ((wouldyoulikeadd=="yes") or (wouldyoulikeadd=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikeadd=="yes":
        AddResult()
    elif wouldyoulikeedit=="yes":
        SaveNewFile()
        
def Main():
    while True:
        wouldyouliketoprint = input("Firstly, would you like to print all of the data for reference? Please enter yes or no: ")
        if not ((wouldyouliketoprint=="yes") or (wouldyouliketoprint=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyouliketoprint=="yes":
        for x in range(len(TestNo)):
            print('{0:2n} {1:4g} {2:g} {3:g}'.format(TestNo[x], TestDate[x], TestTime[x], Result[x]))
        print("The data is in the form: Test Number, Date (dd.mm), Time, Result")
    while True:
        wouldyoulikefull = input("Would you like to analyse the full set of data? Please enter yes or no: ")
        if not ((wouldyoulikefull=="yes") or (wouldyoulikefull=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikefull=="yes":
        FullDataAnalysis()
    while True:
        wouldyoulikepartial = input("Would you like to analyse a specific portion of the data? Please enter yes or no: ")
        if not ((wouldyoulikepartial=="yes") or (wouldyoulikepartial=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikepartial=="yes":
        PartialDataAnalysis()
    while True:
        wouldyoulikesearch = input("Would you like to search for a specific result to view or edit? Please enter yes or no: ")
        if not ((wouldyoulikesearch=="yes") or (wouldyoulikesearch=="no")):
            print("Not a yes or no! Please try again. ")
        else:
            break
    if wouldyoulikesearch=="yes":
        BinarySearch()
    else:
        while True:
            wouldyoulikeadd = input("Would you like to add a new result to the data? Please enter yes or no: ")
            if not ((wouldyoulikeadd=="yes") or (wouldyoulikeadd=="no")):
                print("Not a yes or no! Please try again. ")
            else:
                break
        if wouldyoulikeadd=="yes":
            AddResult()
     
print("Welcome to the program.\nThis program will allow the user to analyse a given set of data through a yes/no flowchart.")    
Main()
while True:
    finished = input("Program is complete, would you like to start again? Please enter yes or no: ")
    if not ((finished=="yes") or (finished=="no")):
        print("Not a yes or no! Please try again. ")
    else:
        break
if finished == "yes":
    Main()
