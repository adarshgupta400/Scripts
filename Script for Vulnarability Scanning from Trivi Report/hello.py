import jsonRead

fileName ="triviConsol.txt"
delimeter = '='
#delimeterColon = ':'

file= open(fileName, 'r')

#Striping specific Value from text file.
def findValue(fullstring): 
    fullstring = fullstring.rstrip('\n')
    value = fullstring[fullstring.index(delimeter)+1 : ] 
    value = value.replace(" ","")
    return value

"""print(jsonRead.giveCoverage())
"""
#Methods to check values
def CheckCoverage(valueToBeChecked):
    if(valueToBeChecked < int(jsonRead.giveCoverage()) ):
        print("Breaking the Build as Coverage in new code " " is less than "+str(jsonRead.giveCoverage()))

def CheckCritical(valueToBeChecked):
    if(valueToBeChecked != 0):
        print("Breaking the Build as there exists "+str(valueToBeChecked)+" critical vulnerability")

def CheckHigh(valueToBeChecked):
    if(valueToBeChecked != 0):
        print("Breaking the Build as there exists "+str(valueToBeChecked) + " highs")

#Scanning text file line by line
for line in file: 
    if line.rfind('coverage') != -1:
        coverage = findValue(line)
        CheckCoverage(int(coverage))

    if line.startswith('high'):
        high = findValue(line)
        CheckHigh(int(high))

    if line.startswith('critical'):
        critical = findValue(line)
        CheckCritical(int(critical))

