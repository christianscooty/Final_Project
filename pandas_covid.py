
########### Takig covid_crime1 and coverting it to more usable format
import pandas as pd
coviddata = pd.read_csv('covid_crime.csv','r',delimiter = ',')

reshape = pd.pivot_table(coviddata, index = ['Date'], columns = 'Crime',values = 'Cases', aggfunc='count', margins = True)

reshape.to_csv('pandas_covid.csv')

######### Going through Covid Case data and and making a dictionary of Date, Cases key value pairs

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
        covdate = dat
        dic[covdate] = str(row[1])
        covid_list_dic.append(dic)
    n += 1

##### Adding the Case count as a column to the Pandas file

from csv import writer
from csv import reader

ccdata = open('pandas_covid.csv','r')
nccdata = open('final_covid_crime.csv', 'w', newline = '')

csv_reader1 = reader(ccdata)
csv_writer = writer(nccdata, delimiter = ',', lineterminator= '\n')

n = 0
header = ['Date','Felony','Misdemeanor','Violations','All','Cases']
csv_writer.writerow(header)

### Add zero to the front

for row in csv_reader1:
    row[0] = '0' + str(row[0])
    if n > 0:
        for dicti in covid_list_dic:
            if row[0] in dicti.keys():
                row.append(dicti[row[0]])
                csv_writer.writerow(row)      
    n += 1