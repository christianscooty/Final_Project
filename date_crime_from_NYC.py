import csv

#### Get Covid Dates in NYC and change them to 2019 dates

covData = 'final_covid_crime.csv'
cov = open(covData, 'r')
reader = csv.reader(cov)

n=0

covid_dates = []

for row in reader:
    if n > 0:
        date = row[0][0:7] + '19'
        covid_dates.append(date)
    n += 1

#### First filter the Historic data and only choose 2019 data so its easier to manage

import csv, operator
cD = 'NYPD_Complaint_Data_Historic.csv'

c = open(cD, 'r')
reader = csv.reader(c)

ccdata = open('Crime_NYC_2019.csv','w')
writer = csv.writer(ccdata, delimiter=',',lineterminator='\n')
n = 0

for row in reader:
    if '2019' in row[1][6:]:
        date = str(row[1])
        crime = str(row[12])
       
        iwant = [date, crime]
        writer.writerow(iwant)
ccdata.close()

###### Then run through just the 2019 data, and select Crimes which occur only on the Covid dates in NYC

from csv import writer
from csv import reader

cD = 'Crime_NYC_2019.csv'

c = open(cD, 'r')
reader = csv.reader(c)

ccdata = open('Crime_NYC_2019_Covid_date.csv','w')
writer = csv.writer(ccdata, delimiter=',',lineterminator='\n')
header = ['Date','Crime']
writer.writerow(header)
n = 0

for row in reader:
    if n > 0:
        if row[0][1:] in covid_dates:
            date = row[0][1:]
            crime = row[1]
           
            iwant = [date, crime]
            writer.writerow(iwant) 
    n+=1   
ccdata.close()


##### Using pandas, we format the data so it looks better and is easier to manage.

import pandas as pd
coviddata = pd.read_csv('Crime_NYC_2019_Covid_date.csv','r',delimiter = ',')

reshape = pd.pivot_table(coviddata, index = ['Date'], columns = 'Crime', values = 'Cases', aggfunc='count', margins = True)

reshape.to_csv('pandas_covid_2019.csv')
