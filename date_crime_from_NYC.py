
import csv
#### Get Covid Dates dates for 2019 and make a list

covData = 'final_covid_crime.csv'
cov = open(covData, 'r')
reader = csv.reader(cov)

n=0

covid_dates = []
for row in reader:
    if n > 0:
        if '02/29' in row[0]:
            row[0] = '3/1/2020'
        covid_dates.append(row[0])
    n += 1
print(covid_dates)


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
        
        if date[3] == '0':
            date = date[0:3] + date[4:]
        if date[0] == '0':
            date = date[1:]
        
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
        splitt = row[0].split("/")
        date = splitt[0] + "/" + splitt[1] + "/" +'2020'
      
        if date in covid_dates:
            date = row[0]
            crime = row[1]
           
            iwant = [date, crime]
            writer.writerow(iwant) 
    n+=1   
ccdata.close()

import csv
covData = 'COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv'
cov = open(covData, 'r')
reader = csv.reader(cov)

n=0

covid_list_dic = []

for row in reader:
    if n > 0:
        dic = {}
        
        dat = row[0].split(" ")[0]
        
        dat = dat[0:6] + '2019'
        print(dat)
        if '02/29' in dat:
            dat = '03/01/2019'
        if dat[3] == '0':
            dat = dat[0:3] + dat[4:]
        if str(dat[0]) == '0':
            covdate = dat[1:]
        
            dic[covdate] = str(row[1])
            covid_list_dic.append(dic)
    n += 1
print(covid_list_dic)

from csv import writer
from csv import reader

ccdata = open('Crime_NYC_2019_Covid_Date.csv','r')
nccdata = open('Crime_NYC_2019_Covid_Date_and_Covid.csv', 'w', newline = '')

csv_reader1 = reader(ccdata)
csv_writer = writer(nccdata, delimiter = ',', lineterminator= '\n')

n = 0
header = ['Date','Crime','Cases']
csv_writer.writerow(header)

for row in csv_reader1:
    if n > 0:
        for dicti in covid_list_dic:
            if row[0] in dicti.keys():
                row.append(dicti[row[0]])
                csv_writer.writerow(row)      
    n += 1

##### Using pandas, we format the data so it looks better and is easier to manage.

import pandas as pd
coviddata = pd.read_csv('Crime_NYC_2019_Covid_Date_and_Covid.csv','r',delimiter = ',')

reshape = pd.pivot_table(coviddata, index = ['Date'], columns = 'Crime', values = 'Cases', aggfunc= 'count')

reshape.to_csv('pandas_covid_2019.csv')

