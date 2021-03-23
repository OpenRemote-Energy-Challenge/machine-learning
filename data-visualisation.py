#Data visualisation python code
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as pyplot

#Check versions of libraries for debugging purposes
print("Python:\t", sys.version.split(' ')[0])
print("Version:", sys.version_info, "\n")

solar_data = pd.read_csv("./SolarData.csv")

print(solar_data.info(), "\n" ,solar_data.describe(), "\n")

#Get how many field values their are in the csv
for field in solar_data:
    print("******** Field:", field, "********")
    print(solar_data[field].value_counts())
    print()

#Split date & time into seperate fields
solar_data['date'] = [datetime.split(' ')[0][2:].strip() for datetime in solar_data['timestamp']]
solar_data['time'] = [datetime.split(' ')[1].strip() for datetime in solar_data['timestamp']]
print(solar_data)

