
from csv import reader

ccdata = open('pandas_covid_2019.csv','r')

csv_reader1 = reader(ccdata)

nccdata = open('pandas_covid.csv','r')

csv_reader2 = reader(nccdata)

casesdata = open('COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv','r')

csv_reader3 = reader(casesdata)


sumf2 = 0
sumv2 = 0
summ2 = 0
sumf9 = 0
sumv9 = 0
summ9 = 0
sumallcrimessunday = 0
sumallcrimesweek = 0

n = 0
for row in csv_reader1:
    if n > 0: 
        sumf9 += int(row[1])
        summ9 += int(row[2])
        sumv9 += int(row[3])
        
    n += 1
    
averagef9 = round(sumf9/(n-1),0)
averagev9 = round(sumv9/(n-1),0)
averagem9 = round(summ9/(n-1),0)
n = 0    
i = 0
w = 0
for row in csv_reader2:
    if n > 0: 
        sumf2 += int(row[1])
        summ2 += int(row[2])
        sumv2 += int(row[3])
        
        if n == 2 or n == 8 or n % 7 == 1 and n < 215:
            sumallcrimessunday += int(row[1]) + int(row[2]) + int(row[3]) 
            i += 1
        
        else:
            sumallcrimesweek += int(row[1]) + int(row[2]) + int(row[3]) 
            w += 1
    n += 1

averagef2 = round(sumf2/(n-1),0)
averagev2 = round(sumv2/(n-1),0)
averagem2 = round(summ2/(n-1),0)
avgsundaycrimes = round(sumallcrimessunday/i,0)
avgcrimesweek = round(sumallcrimesweek/w,0)
####################3
saturdaycases = 0
sundaycases = 0
mondaycases = 0
tuesdaycases = 0
wednesdaycases = 0
thursdaycases = 0
fridaycases = 0

n = 1
for row in csv_reader3:
    if n > 1: 
        if n == 2 or n % 7 == 0 and n < 215:
            saturdaycases += int(row[1])           
        if n == 8 or n % 7 == 1 and n != 1 and n < 215:
            sundaycases += int(row[1])           
        if n ==9 or n % 7 == 2 and n != 2 and n < 215:
            mondaycases += int(row[1])
        if n == 3 or n % 7 == 3 and n < 215:
            tuesdaycases += int(row[1])
        if n == 4 or n % 7 == 4 and n < 215:
            wednesdaycases += int(row[1])
        if n == 5 or n % 7 == 5 and n < 215:
            thursdaycases += int(row[1])
        if n == 6 or n % 7 == 6 and n < 215:
            fridaycases += int(row[1])
    n += 1

header = ['2020 Avg Felony','2020 Avg Misdemeanors','2020 Avg Violations', '2019 Avg Felony','2019 Avg Misdemeanors','2019 Avg Violations']
values = [averagef2,averagem2,averagev2,averagef9,averagem9,averagev9]


weekdaycases = [saturdaycases,sundaycases,mondaycases,tuesdaycases,wednesdaycases,thursdaycases,fridaycases]

percentf = round(100*(averagef9-averagef2)/averagef9,2)
percentm = round(100*(averagem9-averagem2)/averagem9,2)
percentv = round(100*(averagev9-averagev2)/averagev9,2)

print(percentf,percentm,percentv)

print(header, values)
#print('Average Sunday Crimes: ', avgsundaycrimes)
#print('Average Crimes during week: ', avgcrimesweek)
print(weekdaycases)
