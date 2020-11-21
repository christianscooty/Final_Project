
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

ccdata = open('Crime_NYC.csv','r')
nccdata = open('covid_crime.csv', 'w', newline = '')

csv_reader1 = reader(ccdata)
csv_writer = writer(nccdata, delimiter = ',', lineterminator= '\n')

n = 0
header = ['Date','Crimes','Cases']
csv_writer.writerow(header)


for row in csv_reader1:
    if n > 0:
        for dicti in covid_list_dic:
            date = row[0]
            if date in dicti.keys():
                date = str(date)
                row.append(dicti[date])
                csv_writer.writerow(row) 
    n += 1