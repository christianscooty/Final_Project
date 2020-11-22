## Appendix 

# Files from NYC Database

* NYPD_Complaint_Data_Current__Year_To_Date_.csv
* COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv 
* NYPD_Complaint_Data_Historic.csv

# Python Files

* extract_covid_crime_info.py - reads from NYPD_Complaint_Data_Current__Year_To_Date_.csv and creates file, Crime_NYC.csv, with two columns, Date and Crime_NYC.csv
* combined_covid_file.py - reads from COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv and Crime_NYC.csv and creates a dictionary of key-value pairs with Date and Cases. Then writes a new file covid_crime.csv with Date, Crime, and Cases.
* pandas_covid.py - reads covid_crime.csv and uses pandas module to create pandas_covid.csv. Then we read pandas_covid.csv and COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv, making a diciontary using key-value pairs with Date and Cases to create final_covid_crime.csv which has the Date, Felony, Misdemeanors, Violations, and Cases as separate columns. 


* date_crime_from_NYC.py - this basically follows all the steps from above, but applies these steps to 2019 data and does so in a single file. First, it reads NYPD_Complaint_Data_Historic.csv and selects only 2019 data to make the process more manageable, putting it into a new csv falled Crime_NYC_2019.csv. Then, we read Crime_NYC_2019.csv and final_covid_crime.csv, create a list of COVID dates from final_covid_crime.csv, then write to a new file, Crime_NYC_2019_Covid_date.csv, where the dates from the list match the dates from the Crime_NYC_2019.csv. At this point, we have a file which has the 2019 dates which correspond with COVID dates, and we have all the crimes from 2019 which are associated with those dates. Next, we have to add the COVID cases numbers (so pandas will work). Just as before,  we read Crime_NYC_2019_Covid_date.csv and COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv, making a diciontary using key-value pairs with Date and Cases to create Crime_NYC_2019_Covid_Date_and_Covid.csv which has the Date, Felony, Misdemeanors, Violations, and Cases as separate columns. Finally, we can use the pandas module to create pandas_covid_2019.csv, so we can analyze the data easier. 





