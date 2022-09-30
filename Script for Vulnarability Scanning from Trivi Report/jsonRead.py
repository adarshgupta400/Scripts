import json

#opening json file
file = open('threshold.json')

# load return JSON obj as Dictionary
data = json.load(file)
#data = json.loads(file.read())
def giveCoverage():
    #for key,value in data.items() :
    #    print(key , value)

    coverage = data['coverage']  #coverage is int
    #print("hjfyuyfjh "+str(coverage))
    return int(coverage)

def giveHigh():
    high = data['high']
    return int(high)

def giveCritical():
    critical = data['high']
    return int(critical)

"""
print(giveCoverage())
print(giveHigh())
print(giveCritical())
"""

file.close()
