from csv import reader
import operator

#####################################
covidcrime = open('covid_crime.csv', 'r')

csv_reader = reader(covidcrime)

covidhistcrimes = {}

n = 0

for row in csv_reader:
    k = row[1]
    if n > 0:
        if k not in covidhistcrimes.keys():
            covidhistcrimes[row[1]] = 1
        elif k in covidhistcrimes.keys():
            covidhistcrimes[row[1]] += 1
    n += 1
    

sortedhistcrimes = sorted(covidhistcrimes.items(), key = operator.itemgetter(1), reverse=True)
print("\n Types of Crimes: \n", sortedhistcrimes)
covidcrime.close()
#####################################

covidcrime = open('covid_crime.csv', 'r')

csv_reader = reader(covidcrime)
   
covidhisttotal = {}                  
n = 0
for row in csv_reader:
    k = row[0]
    if n > 0:
    
        if k in covidhisttotal.keys():
            covidhisttotal[k] += 1
        else:
            covidhisttotal[k] = 1
    n += 1
sortedhisttotal = sorted(covidhisttotal.items(), key = operator.itemgetter(1), reverse=True)

print("Total crimes by date: \n", sortedhisttotal)
covidcrime.close()
#####################################
covidcrime = open('covid_crime.csv', 'r')

csv_reader = reader(covidcrime)

covidhistfelony = {}

n = 0

for row in csv_reader:
    k = row[0]
    if n > 0:
        if k not in covidhistfelony.keys() and 'F' in row[1]:
            covidhistfelony[row[0]] = 1
        elif k in covidhistfelony.keys() and 'F' in row[1]:
            covidhistfelony[row[0]] += 1
    n += 1

sortedhistfelony = sorted(covidhistfelony.items(), key = operator.itemgetter(1), reverse=True)
print("\n Felonies by date: \n", sortedhistfelony)
covidcrime.close()
#####################################
covidcrime = open('covid_crime.csv', 'r')

csv_reader = reader(covidcrime)

covidhistmisdemeanor = {}

n = 0

for row in csv_reader:
    k = row[0]
    if n > 0:
        if k not in covidhistmisdemeanor.keys() and 'M' in row[1]:
            covidhistmisdemeanor[row[0]] = 1
        elif k in covidhistmisdemeanor.keys() and 'M' in row[1]:
            covidhistmisdemeanor[row[0]] += 1
    n += 1

sortedhistmisdemeanor = sorted(covidhistmisdemeanor.items(), key = operator.itemgetter(1), reverse=True)
print("\n Misdemeanors by date: \n", sortedhistmisdemeanor)
covidcrime.close()
#####################################
covidcrime = open('covid_crime.csv', 'r')

csv_reader = reader(covidcrime)

covidhistviolations = {}

n = 0

for row in csv_reader:
    k = row[0]
    if n > 0:
        if k not in covidhistviolations.keys() and 'V' in row[1]:
            covidhistviolations[row[0]] = 1
        elif k in covidhistviolations.keys() and 'V' in row[1]:
            covidhistviolations[row[0]] += 1
    n += 1

sortedhistviolations = sorted(covidhistviolations.items(), key = operator.itemgetter(1), reverse=True)
print("\n Violations by date: \n", sortedhistviolations)
covidcrime.close()




