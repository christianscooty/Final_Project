##### First, we go through the Complaint data and create a csv with only the date and the crime information

import csv, operator
cD = 'NYPD_Complaint_Data_Current__Year_To_Date_.csv'

c = open(cD, 'r')
reader = csv.reader(c)

ccdata = open('Crime_NYC.csv','w')
writer = csv.writer(ccdata, delimiter=',',lineterminator='\n')
n = 0
for row in reader:
    iwant = []
    

    date = str(row[3])
    
   
    if date[3] == '0':
        date = date[0:3] + date[4:]
    if date[0] == '0':
        date = date[1:]
       
    crime = str(row[13])
    
    iwant = [date, crime]
    
    writer.writerow(iwant)
    
    n+=1
    